# 10 — Statistiques & Probabilités

Module de 9 jours sur les bases de la statistique appliquée à la data science : analyse exploratoire (EDA), séries temporelles et tests d'hypothèses, sur des jeux de données réels.

## Compétences
- Connaître et savoir utiliser les principaux descripteurs statistiques
- Identifier et comprendre des liens entre différentes variables
- Analyser une série temporelle
- Connaître des fonctions pour manipuler et analyser des séries temporelles (`resample`, `interpolate`, `seasonal_decompose`, `rolling`)
- Réaliser un test de comparaison et un test d'indépendance
- Réaliser des tests d'hypothèses pertinents et les interpréter

## Contenu

### Atelier 1 : EDA sur Gapminder (espérance de vie et revenu par pays)
- Chargement, inspection des types, valeurs manquantes et doublons
- Nettoyage du dataset de revenus (valeurs abrégées type `15.6k`, fonction `to_real_number()`)
- **Statistiques univariées** : min/max, moyenne, médiane, mode, histogrammes, boxplots, étendue, IQR, variance, écart-type, skewness, kurtosis
- **Statistiques multivariées** : normalisation et standardisation, détection d'outliers, scatter plots, corrélations (heatmap, évolution de la corrélation revenu / espérance de vie)

### Atelier 2 : Séries temporelles sur Air Passengers
- `DateTimeIndex`, sélection par année, ajustement par nombre de jours du mois
- Rééchantillonnage (`resample`) et interpolation (`interpolate`)
- Décomposition tendance / saisonnalité / résidus avec `seasonal_decompose` (modèles additif et multiplicatif), moyenne mobile (`rolling`)

### Atelier 3 : Projet RTE éCO2mix (consommation et production électrique en France)
- Chargement, nettoyage et préparation de données réelles (données nationales et régionales)
- Exploration nationale : mix énergétique, autonomie, équilibre du réseau, saisonnalité, lien avec les émissions de CO2
- Exploration régionale : consommation, production renouvelable et non renouvelable, autonomie, comparaison par habitant et par km²
- Présentation orale d'une question exploratoire

### Tests d'hypothèses
- Test de comparaison (ex : Titanic, taux de survie selon la classe)
- Test d'indépendance (ex : Titanic, lien entre genre et classe)
- Mini-infographie sur le jeu de données de l'enquête sur le bonheur, avec au moins 2 tests d'hypothèses

## Stack technique
Python · pandas · NumPy · Matplotlib · seaborn · SciPy · statsmodels · Jupyter

## Notebooks

- EDA Gapminder
- Séries temporelles Air Passengers
- Projet RTE éCO2mix
- Tests d'hypothèses (Titanic, enquête sur le bonheur) et infographie
