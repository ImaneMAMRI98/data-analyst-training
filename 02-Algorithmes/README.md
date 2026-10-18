# 02 — Algorithmique

Module d'algorithmique autour d'une problématique : **le tri**.
Méthodologie de conception (spécification, conception préliminaire et détaillée, codage), pseudo-code, complexité et organisation du code en module Python.

## Compétences
- Méthodologie de conception d'une solution informatique : écrire et lire du pseudo-code, de la conception préliminaire au codage Python
- Analyse de la complexité d'un algorithme (notation grand O, comparaison avec la sortie de `%prun`)
- Création d'une bibliothèque Python : organisation du code sous forme de module réutilisable

## Contenu

### Itération 1 — Introduction à l'algorithmique
- **Algo avec des cartes** : conception préliminaire et détaillée (signatures + pseudo-code) d'un algorithme de tri d'un paquet de cartes (séparation par couleur, tri de chaque tas par insertion, assemblage), avec une numérotation à partir de l'index zéro
- **Codage en Python** de l'algorithme conçu
- **Tris classiques** : tri à bulles, tri par insertion, tri par sélection ; fonction vs procédure, complexité O, analyse avec les magic commands (`%prun`)

### Itération 2 — Les tris récursifs
- **Atelier récursivité** : factorielle, suite de Fibonacci (versions récursive et itérative), conjecture de Syracuse, PGCD (algorithme d'Euclide), avec profilage `%time %prun`
- **Paradigme « Diviser pour régner »**
- **Tri fusion** (merge sort)
- **Tri rapide** (quick sort), avec le notion de pivot et son impact sur la complexité

### Itération 3 — Module Python et comparaison des complexités
- **Création du module `sorting.py`** regroupant les tris classiques et récursifs, importable depuis n'importe quel notebook
- **Comparaison empirique des complexités** des algorithmes sur des tableaux de tailles différentes, visualisée sous forme de figure

## Complexités des algorithmes de tri

| Algorithme | Meilleur cas | Cas moyen | Pire cas |
|---|---|---|---|
| Tri à bulles | O(n) *(version optimisée)* / O(n²) | O(n²) | O(n²) |
| Tri par insertion | O(n) | O(n²) | O(n²) |
| Tri par sélection | O(n²) | O(n²) | O(n²) |
| Tri fusion | O(n log n) | O(n log n) | O(n log n) |
| Tri rapide | O(n log n) | O(n log n) | O(n²) |

## Fichiers
- `sorting.py` : module contenant `bubble_sort`, `insertion_sort`, `selection_sort`, `merge_sort`, `quick_sort` et les fonctions d'aide (`generate_random_array`, `swap`, `fusionner`, `partitionner`)
- `AlgosTriClassiques.ipynb` : tris classiques
- `AlgosTriRecursifs.ipynb` : tris récursifs
- `atelier_recursivite.ipynb` : atelier récursivité
- `sorting_tests.ipynb` : tests et import du module `sorting`
- `CorrectionAlgo.ipynb`

## Pseudo-code : tri d'un paquet de cartes

```
Function ordonner_tas(tas) :
DEBUT
  n = taille(tas)
  pour i de 1 à n-1 :
    carte = tas[i]
    j = i
    tantque j > 0 et valeur(tas[j-1]) > valeur(carte) :
      tas[j] = tas[j-1]
      j = j-1
    tas[j] = carte
FIN

algorithme trie_cartes :
DEBUT
  // SÉPARER LES CARTES
  tas_C, tas_T, tas_K, tas_P = [], [], [], []
  pour chaque carte de paquet :
    insérer carte dans le tas correspondant à sa couleur
  // TRIER LES CARTES
  ordonner_tas(tas_C) ; ordonner_tas(tas_T)
  ordonner_tas(tas_K) ; ordonner_tas(tas_P)
  // ASSEMBLER LES TAS
  insérer (tas_C, tas_T, tas_K, tas_P, joker) dans paquet_trie
FIN
```
