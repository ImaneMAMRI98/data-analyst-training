import json
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
from airflow.decorators import dag, task

DOSSIER_DONNEES = Path("/opt/airflow/data")   # le dossier data/ vu DEPUIS le conteneur
FICHIER_SOURCE = DOSSIER_DONNEES / "entreprises_isere.csv"
DOSSIER_RUNS = DOSSIER_DONNEES / "runs"

SEUIL_MIN_LIGNES = 5000   # en dessous : on considère l'extraction incomplète


def dossier_du_run(ds):
    """Le dossier de CE run, créé s'il n'existe pas."""
    chemin = DOSSIER_RUNS / ds
    chemin.mkdir(parents=True, exist_ok=True)
    return chemin


@dag(
    dag_id="atelier_pipeline_date_new",
    schedule="@daily",
    start_date=datetime(2026, 7, 20),
    catchup=True,
    max_active_runs=1,
    default_args={"retries": 2, "retry_delay": timedelta(seconds=30)},
    tags=["atelier"],

)
def atelier_pipeline_date_new():

    @task
    def preparer(ds=None):
        """Fige la source dans le dossier daté du run (le « snapshot » du jour)."""
        dossier = dossier_du_run(ds)
        source = pd.read_csv(FICHIER_SOURCE)
        snapshot = source.sample(frac=0.9, random_state=int(ds.replace("-", "")))
        snapshot.to_csv(dossier / "entreprises.csv", index=False)
        print(f"[{ds}] snapshot : {len(snapshot)} lignes")


    @task

    def par_commune(ds=None):
        # TODO lire dossier_du_run(ds) / "entreprises.csv"
        # TODO extraire la commune depuis la colonne "localisation"
        #      ("38320 BRIE-ET-ANGONNES" → code postal + commune)
        # TODO compter les entreprises par commune, trier, écrire par_commune.csv
        dossier = dossier_du_run(ds)
        df = pd.read_csv(dossier / 'entreprises.csv')

        df['commune'] = df['localisation'].str.split(' ', n=1, expand=True)[1]

        compte = (
            df.groupby('commune')
            .size()
            .reset_index(name='nb_entreprises')
            .sort_values('nb_entreprises', ascending=False)
        )

        compte.to_csv(dossier / "par_commune.csv", index=False)
        print(f"[{ds}] {len(compte)} communes")

    @task
    def controle_qualite(ds=None):
        # TODO calculer : nb de lignes, doublons de siren, localisations vides
        # TODO écrire ces indicateurs dans qualite.json
        # TODO lever une erreur (raise ValueError) si nb de lignes < SEUIL_MIN_LIGNES
        dossier = dossier_du_run(ds)
        df = pd.read_csv(dossier / 'entreprises.csv')
        nb_lignes = len(df)
        if nb_lignes < SEUIL_MIN_LIGNES:
            raise ValueError(f"Pas assez de lignes : {nb_lignes} < {SEUIL_MIN_LIGNES}")
        doublons = int(df['siren'].duplicated().sum())
        nb_vides = int(df['localisation'].isna().sum())

        qualite = {
        "nb_lignes": nb_lignes,
        "doublons_siren": doublons,
        "localisations_vides": nb_vides,
        }

        
        with open(dossier / "qualite.json", "w") as f:
            json.dump(qualite, f, indent=2)

        return qualite

    @task
    def rapport(ds=None):
        # TODO relire par_commune.csv et qualite.json
        # TODO écrire rapport.md : les chiffres clés + le top 5 des communes
        dossier = dossier_du_run(ds)

        df = pd.read_csv(dossier / "par_commune.csv")
        qualite = pd.read_json(dossier / "qualite.json", typ="series")

        col_count = "nb_entreprises"
        top5 = df.sort_values(col_count, ascending=False).head(5)

        lignes = [
            "# Rapport\n",
            f"- Lignes traitées : {qualite['nb_lignes']}",
            f"- Doublons SIREN : {qualite['doublons_siren']}",
            f"- Localisations vides : {qualite['localisations_vides']}\n",
            "## Top 5 communes\n",
        ]
        for _, row in top5.iterrows():
            lignes.append(f"- {row['commune']} : {row[col_count]}")

        with open(dossier / "rapport.md", "w") as f:
            f.write("\n".join(lignes))

        return str(dossier / "rapport.md")

    # TODO câbler le diamant (section 3) : preparer, puis les deux branches
    #      en parallèle, puis rapport qui attend les DEUX
    preparer() >> [par_commune(),controle_qualite()] >> rapport()


atelier_pipeline_date_new()