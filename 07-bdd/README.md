# 07 — Bases de données / SQL

Module de 6 jours autour d'un projet fil rouge : la base de données **NumCity**, une ville fictive dont on recense les lieux utiles aux citoyens (parkings vélos et trottinettes, bornes de recharge, fontaines, toilettes publiques, parcs...). Du cahier des charges jusqu'à l'exploitation des données en Python.

## Compétences
- Définir une base de données SQL et noSQL
- Installer son environnement de travail (PostgreSQL + client SQL)
- Concevoir une base de données SQL (méthode Merise)
- Écrire des scripts SQL de création et d'insertion
- Écrire les requêtes SQL de base
- Écrire un script Python permettant de se connecter à une base de données
- Mettre en œuvre un ORM Python
- Afficher des données d'une base de données sur une carte
- Créer un mémo

## Contenu

### Itération 1 — Découverte des bases de données
- Types de bases de données : relationnelles, NoSQL (clé-valeur, documentaire, colonnes, graphe), en mémoire, distribuées
- Théorème CAP et critères de choix d'un SGBD
- Installation de PostgreSQL et d'un client SQL, connexion à la base
- Bonnes pratiques de sécurité d'accès (SSL/TLS, moindre privilège, gestion des mots de passe, journaux d'audit)

### Itération 2 — Conception de la base NumCity
- Analyse du cahier des charges : diagramme de cas d'usage UML et scénarios
- Dictionnaire de données
- Modèle Conceptuel de Données (**MCD**) et Modèle Logique de Données (**MLD**) avec la méthode **Merise**
- Normalisation (1NF, 2NF, 3NF)
- Scripts SQL de création des tables et contraintes, insertion de données de test
- Tests de contraintes et optimisation (index, `EXPLAIN`)

### Itération 3 — Requêtes SQL
- `INSERT`, `SELECT`, `UPDATE`, `DELETE` (avec `RETURNING`)
- Jointures (`JOIN`)
- Agrégations (`COUNT`, `AVG`, `MAX`, `GROUP BY`) et sous-requêtes
- Mémo de requêtes avec captures des résultats

### Itération 4 — Interfaçage Python
- **psycopg2** : connexion, curseurs, exécution de requêtes
- **pandas** : `read_sql_query`, analyses et graphiques avec matplotlib
- **SQLAlchemy** : moteur, sessions, ORM (classes Python mappées sur les tables)
- **folium** : cartes interactives à partir des données géolocalisées

## Stack technique
PostgreSQL · SQL · DBeaver · Looping (Merise) · Python · psycopg2 · pandas · matplotlib · SQLAlchemy · folium

## Fichiers
*(à adapter selon ce que tu déposes dans le dossier)*
- Mémo : types de bases de données, théorème CAP, installation, sécurité
- Schéma NumCity : dictionnaire de données, MCD, MLD
- Scripts SQL : création et insertion de la base
- Mémo de requêtes SQL
- Notebooks : psycopg2, pandas, SQLAlchemy, cartographie
