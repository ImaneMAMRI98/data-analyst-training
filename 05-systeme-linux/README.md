# 05 — Système d'exploitation (Linux)

Module de 3 jours pour découvrir Linux, la ligne de commande, la gestion de paquets et l'automatisation de tâches sur fichiers.

## Compétences
- Installer des paquets et comprendre les dépendances
- Créer, renommer, éditer, supprimer des fichiers et répertoires en ligne de commande
- Gestion automatisée de fichiers dans l'arborescence Linux
- Redirection d'entrées/sorties de programmes pour pré-traiter des données

## Contenu

### Itération 1 — Découverte de Linux
- Déplacement dans l'arborescence en ligne de commande (`cd`, `ls`, `which`)
- Gestion de paquets avec `apt` (`apt update`, installation de `tree` et `tldr`), notion de dépendance
- Commande `sudo`
- Initiation du mémo : fonctionnement d'un OS et de Linux, commandes utiles

### Itération 2 — Pourquoi utiliser Linux ?
- Philosophie du logiciel libre et open source
- Manipulation de fichiers et d'images : `ls`, `mkdir`, `mv`, conversion avec ImageMagick
- Manipulation de PDF : `pdftk` (concaténation, extraction de pages), `poppler-utils` (extraction d'images)
- Pipe et redirections : comptage de fichiers, `ls` + `head`
- Serveur web local à la volée pour partager des fichiers
- Sauvegarde avec `rsync`
- Planification avec **cron** : script Python de renommage automatique des fichiers (minuscules, espaces remplacés par des underscores) exécuté toutes les minutes

### Itération 3 — Gestion automatisée de fichiers (cas WDGAS)
- Tri d'environ 10 000 fichiers `.data` en désordre, répartis par département (BU, HR, IT)
- Script bash `montrieur.sh` : création des dossiers par département, déplacement et renommage des fichiers en `<nom>_<prénom>.data`
- Gestion des droits avec `chmod` pour rendre le script exécutable

### Itération 4 — Entrées/sorties
- **Partie 1** : redirections, `cat` et `wc` pour compter lignes, mots et octets d'un fichier texte (français et anglais)
- **Partie 2** : prétraitement du texte avec `sed` et `grep` (suppression de la ponctuation, des chiffres, des majuscules et des lignes vides), puis comptage des occurrences avec `sort`, `uniq`, `head`, `tail`
  - index complet des mots triés par occurrence
  - top 30 et 30 mots les moins utilisés

## Commandes utilisées
`cd` · `ls` · `mkdir` · `mv` · `which` · `tree` · `tldr` · `apt` · `sudo` · `chmod` · `crontab` · `rsync` · `cat` · `wc` · `sed` · `grep` · `sort` · `uniq` · `head` · `tail`

## Fichiers
- `iteration 1` : mémo des commandes Linux
- `iteration 2` : notes de l'itération 2 (manipulation de fichiers, pipe, rsync, cron)
- `iteration-3/script.sh` : script de tri des fichiers WDGAS par département
- `iteration-3/notes-iteration-3.pdf` : notes de l'itération 3
- `iteration 4/` : commandes utilisées pour les redirections et le comptage de mots
