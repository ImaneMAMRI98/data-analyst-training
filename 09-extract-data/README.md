# 09 — Extraction de données

Module de 14 jours autour d'un projet fil rouge : constituer et industrialiser un jeu de données sur les **entreprises de l'Isère**, en collaboration avec Invest in Grenoble Alpes. Du scraping jusqu'à un pipeline orchestré avec Airflow et alimentant un entrepôt PostgreSQL.

## Compétences
- Scraping avec Scrapy (site bookstore)
- Récupération d'un tableau web (INSEE)
- Pagination avec Selenium
- Utilisation d'API avec paramètres
- Modélisation des données extraites (diagramme UML)
- Normalisation d'un modèle de données
- ETL vs ELT, Data Lake vs Data Warehouse
- Installation et configuration d'Airflow (Docker)
- Pipeline ETL en Python
- Pipeline ETL orchestré avec Airflow (DAG)
- Récupération des coordonnées GPS par commune via l'API geo, export en CSV
- Création d'un DAG Airflow comportant plusieurs tâches

## Contenu

### Itération 1 — Scraping
- Bases du HTML, inspection des pages
- **Scrapy** : projet `bookstore` (titres, pagination, prix, stock), puis scraping des entreprises de l'Isère des secteurs informatique et services d'information (codes NAF 62 et 63)
- **Selenium** : pagination sur un site chargé dynamiquement (annuaire-entreprises.data.gouv.fr)

### Itération 2 — API
- Protocole HTTP, méthodes, format JSON, librairie `requests` (API Lorem Picsum)
- **API Géo** : code postal et coordonnées GPS de chaque commune, export en CSV
- **API Recherche d'entreprises** : collecte des entreprises par localisation, comparaison avec les données scrapées
- **API Sirene (INSEE)** : authentification par token, enrichissement des entreprises à partir du SIREN
- Bonus : API météo Open-Meteo, base PostgreSQL sous Docker, requête SQL sur les nuits tropicales à Valence

### Itération 3 — Modélisation
- Passage de fichiers plats à des entités, attributs, associations et identifiants
- Deux sens de « normaliser » : les valeurs et le modèle
- Redondance, anomalies de mise à jour, d'insertion et de suppression
- Formes normales (1NF, 2NF, 3NF) appliquées à un cas réel, décomposition en deux tables reliées
- Normaliser en Silver, dénormaliser en Gold

### Itération 4 — ETL et orchestration
- **ETL vs ELT**, architecture médaillon (Bronze, Silver, Gold), préparation d'un pipeline sur Databricks Community Edition
- **Docker** : images, conteneurs, `Dockerfile`, `docker compose`
- Lancement d'**Airflow** en local
- Écriture de DAGs : tâches, dépendances (`>>`), planification, templates (`{{ ds }}`), retries, catchup, idempotence
- Atelier : pipeline daté (snapshot, agrégat par commune, contrôle qualité, rapport)
- **Pipeline médaillon** `extract >> bronze >> silver >> gold` vers PostgreSQL

## Architecture du pipeline

| Couche | Contenu |
|---|---|
| Bronze | CSV scrapés et issus d'API, chargés tels quels avec métadonnées |
| Silver | Données nettoyées, typées, dédupliquées, entreprises jointes aux communes (géolocalisation) |
| Gold | Nombre d'entreprises par commune, indicateurs globaux |

## Stack technique
Python · Scrapy · Selenium · requests · pandas · SQLAlchemy · PostgreSQL · Docker · Apache Airflow · Databricks Community Edition

## Fichiers

- Spiders Scrapy et script Selenium
- Scripts API (communes, entreprises, INSEE) et CSV produits
- Schéma du modèle de données
- DAGs Airflow (`dag_atelier.py`, `pipeline_entreprises.py`) et captures de l'interface
