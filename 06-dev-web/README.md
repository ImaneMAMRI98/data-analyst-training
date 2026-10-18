# 06 — Développement Web

Module de 3 jours : conception en équipe d'un site web de génération d'histoires pour enfants, de l'interface HTML/CSS jusqu'à l'intégration d'un LLM local. Le projet livré est un site complet (HTML, CSS, Flask, Ollama).

## Compétences
- Concevoir et développer en équipe un site web en HTML5/CSS3
- Créer un serveur web avec Flask (routes multiples, pages HTML/CSS)
- Interagir avec un LLM open-source en local (Ollama, modèle multimodal)

## Le projet
Un site web multi-pages (accueil + galerie) servi par **Flask**. Chaque image de la galerie est analysée par un LLM local (**Ollama + gemma3**) qui génère automatiquement une histoire pour enfants, affichée sous l'image.

## Contenu

### Itération 1 — Construction du site web
- Maquette papier de la page d'accueil (wireframe)
- Pages `accueil.html` et `gallery.html` en HTML5, mise en forme dans `style.css`
- Galerie d'images en grille avec **Flexbox**
- Navigation entre les pages par liens hypertextes

### Itération 2 — Serveur Flask
- Environnement virtuel Python (`venv`) et fichier `requirements.txt` pour la reproductibilité
- Application Flask avec deux routes : `/` et `/gallery`
- Organisation Flask : dossiers `templates/` et `static/`, `render_template()`, `url_for('static', ...)`
- Galerie dynamique : listing des images du dossier avec le module `os`, affichage avec une boucle **Jinja2**

### Itération 3 — Ollama et IA générative
- Installation d'**Ollama** et du modèle **gemma3**, utilisation en ligne de commande
- Pilotage du modèle depuis Python avec la librairie `ollama` (analyse d'image + prompt)
- Intégration dans la route `/gallery` : une histoire générée par image
- **Cache** des histoires dans un fichier `.pkl` (pickle) pour ne pas les régénérer à chaque chargement

## Stack technique
HTML5 · CSS3 (Flexbox) · Python · Flask · Jinja2 · venv · Ollama (gemma3)

## Structure du projet
- `app.py` : serveur Flask (routes `/` et `/gallery`, appel à Ollama, cache des histoires)
- `imgHist.py`, `ollama_test.py` : essais d'interaction avec Ollama en Python
- `templates/` : `accueil.html`, `gallery.html`
- `static/` : `style.css` et dossier `images/`
- `requirements.txt` : dépendances (Flask, ollama)

## Lancer le projet
1. Installer [Ollama](https://ollama.com) puis le modèle : `ollama pull gemma3`
2. Créer l'environnement : `python -m venv venv`, puis l'activer (`venv\Scripts\activate` sous Windows)
3. Installer les dépendances : `pip install -r requirements.txt`
4. Lancer : `python app.py`, puis ouvrir http://127.0.0.1:5000
