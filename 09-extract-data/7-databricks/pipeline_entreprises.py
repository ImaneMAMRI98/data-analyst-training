from datetime import datetime ,timedelta
import pandas as pd
from sqlalchemy import create_engine, text
from airflow.decorators import dag, task
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
import requests

WAREHOUSE_URL = "postgresql+psycopg2://analyste:analyste@warehouse:5432/entreprises"
DATA_DIR = "/opt/airflow/data"
FICHIER_ENTREPRISES = f"{DATA_DIR}/entreprises_isere.csv"
FICHIER_COMMUNES    = f"{DATA_DIR}/communes_isere.csv"
FICHIER_INSEE    = f"{DATA_DIR}/entreprises_insee_secteur.csv"

def _engine():
    return create_engine(WAREHOUSE_URL)

@dag(dag_id="pipeline_entreprises", schedule="@daily",
     start_date=datetime(2026, 1, 1), catchup=False,
     tags=["etl", "medaillon", "entreprises"],
    default_args={"retries": 2, "retry_delay": timedelta(seconds=30)})
def pipeline_entreprises():

    @task(retries=3, retry_delay=timedelta(seconds=10))
    def tache_qui_echoue():
        raise ValueError("Échec volontaire pour tester les retries")

    @task
    def extract() -> None:                     # ne renvoie rien : chaque task lit sa source
        for nom, c in [("entreprises", FICHIER_ENTREPRISES),
                       ("communes", FICHIER_COMMUNES),
                       ("entreprises_insee", FICHIER_INSEE)]:
            print(f"[extract] {nom}: {len(pd.read_csv(c))} lignes")

    @task
    def bronze() -> None:
        moteur, ts = _engine(), datetime.now()
        ent = pd.read_csv(FICHIER_ENTREPRISES)
        ent["_ingested_at"], ent["_source"] = ts, "scraping_annuaire"
        ent.to_sql("entreprises_isere", moteur, schema="bronze",
                   if_exists="replace", index=False)
        com = pd.read_csv(FICHIER_COMMUNES)
        com["_ingested_at"], com["_source"] = ts, "api_communes"
        com.to_sql("communes", moteur, schema="bronze",
                   if_exists="replace", index=False)
        
        insee = pd.read_csv(FICHIER_INSEE)
        insee["_ingested_at"], insee["_source"] = ts, "scraping_insee"
        insee.to_sql("entreprises_insee", moteur, schema="bronze",
                   if_exists="replace", index=False)

    @task
    def silver() -> None:
        moteur = _engine()
        ent = pd.read_sql("SELECT * FROM bronze.entreprises_isere", moteur)
        com = pd.read_sql("SELECT * FROM bronze.communes", moteur)
        insee = pd.read_sql("SELECT * FROM bronze.entreprises_insee", moteur)
        

        # TODO 1 : découper "38000 GRENOBLE" -> code_postal + commune
        #          (indice : ent["localisation"].str.extract(r"^\s*(\d{5})\s+(.*)$"))
        extrait = ent["localisation"].str.extract(r"^\s*(\d{5})\s+(.*)$")
        ent["code_postal"] = extrait[0]
        ent["commune"] = extrait[1].str.strip().str.upper()

        # TODO 2 : SIREN en texte, jeter les lignes sans siren/code_postal, dédupliquer
        ent["siren"] = ent["siren"].astype(str)
        ent = ent.dropna(subset=["siren", "code_postal"]).drop_duplicates(subset=["siren"])

        # TODO 3 : préparer com (renommer "Code postal"/"Latitude"/"Longitude"),
        #          puis JOINDRE à gauche sur code_postal pour attacher la géoloc
        com = com.rename(columns={
            "Code postal": "code_postal",
            "Latitude": "latitude",
            "Longitude": "longitude",
        })
        com["code_postal"] = com["code_postal"].astype(str)
        com = com.drop_duplicates(subset=["code_postal"])   
        ent = ent.merge(com[["code_postal", "latitude", "longitude"]],
                         on="code_postal", how="left")

        # TODO 4 : garder [siren, nom, code_postal, commune, latitude, longitude]
        #          puis .to_sql("entreprises", moteur, schema="silver",
        #                       if_exists="replace", index=False)
        ent = ent[["siren", "nom", "code_postal", "commune", "latitude", "longitude"]]
        ent.to_sql("entreprises", moteur, schema="silver",
                   if_exists="replace", index=False)

        insee["siren"] = insee["siren"].astype(str)
        insee = insee[insee["etat_administratif"] == "A"]          # garder actifs
        insee = insee.dropna(subset=["siren", "activite_principale"])
        insee = insee.drop_duplicates(subset=["siren"])             # dédupliquer

        insee = insee[["siren", "nom", "activite_principale"]]
        insee.to_sql("entreprises_secteur", moteur, schema="silver",
                    if_exists="replace", index=False)
            
    @task
    def controle_qualite() -> None:
        moteur = _engine()
        df = pd.read_sql("SELECT * FROM silver.entreprises", moteur)
        taux_vides = df["siren"].isna().mean()
        if taux_vides > 0.30:
            raise ValueError(f"Trop de SIREN vides : {taux_vides:.0%}")
        print(f"Contrôle qualité OK : {taux_vides:.1%} de SIREN vides")       

    # @task
    # def gold() -> None:
        # moteur = _engine()
        # with moteur.begin() as conn:
        #     # TODO 5 : TRUNCATE puis INSERT INTO gold.entreprises_par_commune
        #     #          SELECT code_postal, commune, MAX(latitude), MAX(longitude),
        #     #                 COUNT(*) FROM silver.entreprises GROUP BY code_postal, commune
        #     conn.execute(text("TRUNCATE gold.entreprises_par_commune"))
        #     conn.execute(text("""
        #         INSERT INTO gold.entreprises_par_commune
        #             (code_postal, commune, latitude, longitude, nb_entreprises)
        #         SELECT code_postal, commune, MAX(latitude), MAX(longitude), COUNT(*)
        #         FROM silver.entreprises
        #         GROUP BY code_postal, commune
        #     """))

        #     # TODO 6 : TRUNCATE puis remplir gold.indicateurs (nb_entreprises,
        #     #          nb_communes, nb_entreprises_geolocalisees)
        #     conn.execute(text("TRUNCATE gold.indicateurs"))
        #     conn.execute(text("""
        #         INSERT INTO gold.indicateurs (indicateur, valeur)
        #         SELECT 'nb_entreprises', COUNT(*) FROM silver.entreprises
        #         UNION ALL
        #         SELECT 'nb_communes', COUNT(DISTINCT code_postal) FROM silver.entreprises
        #         UNION ALL
        #         SELECT 'nb_entreprises_geolocalisees', COUNT(*)
        #         FROM silver.entreprises WHERE latitude IS NOT NULL
        #     """))

        #     conn.execute(text("TRUNCATE gold.entreprises_par_activite"))
        #     conn.execute(text("""
        #         INSERT INTO gold.entreprises_par_activite (activite_principale, nb_entreprises)
        #         SELECT activite_principale, COUNT(*)
        #         FROM silver.entreprises_secteur
        #         GROUP BY activite_principale
        #     """))
    gold_entreprises_par_commune = SQLExecuteQueryOperator(
        task_id="gold_entreprises_par_commune",
        conn_id="warehouse",
        sql=[
            "TRUNCATE gold.entreprises_par_commune",
            """
            INSERT INTO gold.entreprises_par_commune
                (code_postal, commune, latitude, longitude, nb_entreprises)
            SELECT code_postal, commune, MAX(latitude), MAX(longitude), COUNT(*)
            FROM silver.entreprises
            GROUP BY code_postal, commune
            """,
        ],
    )

    gold_indicateurs = SQLExecuteQueryOperator(
        task_id="gold_indicateurs",
        conn_id="warehouse",
        sql=[
            "TRUNCATE gold.indicateurs",
            """
            INSERT INTO gold.indicateurs (indicateur, valeur)
            SELECT 'nb_entreprises', COUNT(*) FROM silver.entreprises
            UNION ALL
            SELECT 'nb_communes', COUNT(DISTINCT code_postal) FROM silver.entreprises
            UNION ALL
            SELECT 'nb_entreprises_geolocalisees', COUNT(*)
            FROM silver.entreprises WHERE latitude IS NOT NULL
            """,
        ],
    )

    gold_entreprises_par_activite = SQLExecuteQueryOperator(
        task_id="gold_entreprises_par_activite",
        conn_id="warehouse",
        sql=[
            "TRUNCATE gold.entreprises_par_activite",
            """
            INSERT INTO gold.entreprises_par_activite (activite_principale, nb_entreprises)
            SELECT activite_principale, COUNT(*)
            FROM silver.entreprises_secteur
            GROUP BY activite_principale
            """,
        ],
    )
    # que du >> : l'ordre seul, aucune donnée ne circule entre les tâches
    tache_qui_echoue()
    extract() >> bronze() >> silver() >> controle_qualite() >> [
        gold_entreprises_par_commune,
        gold_indicateurs,
        gold_entreprises_par_activite,
    ]


pipeline_entreprises()