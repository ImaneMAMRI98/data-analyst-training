# 11 — Machine Learning

Parcours en plusieurs modules : de la régression linéaire jusqu'au Deep Learning, avec des projets réalisés sur des données réelles (notamment les arbres de la ville de Grenoble).

## Compétences
- Réaliser et interpréter une régression linéaire avec Python
- Mener un projet de Machine Learning de bout en bout
- Utiliser des pipelines scikit-learn pour prétraiter les données
- Comparer plusieurs algorithmes (arbre de décision, forêt aléatoire, SVM)
- Régler les hyperparamètres et évaluer un modèle
- Créer de nouvelles features et mesurer leur impact
- Entraîner et évaluer des modèles de classification et de clustering
- Utiliser le bagging et le boosting
- Construire des réseaux de neurones, dont un CNN avec Transfer Learning


## Contenu

### Module 0 : Régression linéaire
- Choix entre approche statistique classique et prédiction ML
- Régression linéaire multiple avec **statsmodels** (coefficients, p-values, intervalles de confiance, R²)
- Sélection de variables par **backward selection**
- Termes clés : intercept, pente, résidus, apprentissage supervisé / non supervisé, overfitting / underfitting, compromis biais-variance
- Calcul du **MSE**, régression avec **scikit-learn** (`fit` / `predict`, erreurs d'entraînement et de test)
- **Validation croisée k-fold**
- Régularisation (**Ridge**, **Lasso**, **ElasticNet**) et recherche d'hyperparamètres avec **GridSearch**

### Module 1 : Introduction au Machine Learning
Projet de bout en bout sur les arbres ouverts de Grenoble : prédire l'**année de plantation** des arbres.
- Nettoyage des données, split entraînement / test, modèle naïf de référence
- **Pipelines** scikit-learn (variables continues et catégorielles, valeurs manquantes, mise à l'échelle)
- Arbres de décision, forêts aléatoires, SVM
- Réglage d'hyperparamètres avec `GridSearchCV`
- Création de nouvelles features
- Explication du fonctionnement des algorithmes en termes simples

### Module 2 : Classification et Clustering
- Entraînement et évaluation d'un modèle de classification
- Métriques adaptées (precision / recall, seuil de décision)
- Importance des variables
- Méthodes d'ensemble : **bagging** et **boosting**
- Clustering et analyse de **silhouette**

### Module 3 : Algorithmes de Machine Learning
Approfondissement du fonctionnement de certains algorithmes.
- Hyperparamètres qui « régulent » les **arbres de décision**, les **forêts aléatoires** et les **SVM**
- Visualisation d'un arbre de décision (exemple sur le jeu de données Iris : séparation par la longueur puis la largeur des pétales, indice de Gini)
- **Courbes d'apprentissage** pour évaluer les performances d'un modèle et repérer sur/sous-apprentissage
- Implémentation de l'algorithme de clustering **k-means** from scratch

### Module 4 : Introduction au Deep Learning
- Réseau de neurones construit from scratch, puis avec **Keras**
- Réseau de neurones convolutifs (**CNN**)
- **Transfer Learning** avec un CNN pré-entraîné

## Stack technique
Python · pandas · NumPy · statsmodels · scikit-learn · Keras · Matplotlib · Jupyter

## Notebooks
- Projet arbres de Grenoble (ML Intro)
- Classification et clustering
- Deep Learning
