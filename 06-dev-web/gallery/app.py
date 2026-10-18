from flask import Flask, render_template
import os
import ollama
import pickle

app = Flask(__name__)

CACHE_FILE = 'histoires_cache.pkl'

def charger_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'rb') as f:
            return pickle.load(f)
    return {}

def sauvegarder_cache(cache):
    with open(CACHE_FILE, 'wb') as f:
        pickle.dump(cache, f)

def generer_histoire(image_path):
    response = ollama.chat(
        model='gemma3',
        messages=[
            {
                'role': 'system',
                'content': 'Tu es un auteur de livres pour enfants. Réponds uniquement en français.'
            },
            {
                'role': 'user',
                'content': """Écris uniquement une courte histoire pour enfants inspirée de cette image.
Commence directement par l'histoire, sans introduction, sans titre, sans commentaire final.
Termine par "Fin." et rien d'autre.""",
                'images': [image_path]
            }
        ]
    )
    return response['message']['content']

@app.route('/')
def hello():
    return render_template('accueil.html')

@app.route('/gallery')
def gallery():
    dossier = 'static/images'
    images = os.listdir(dossier)
    
    cache = charger_cache()
    
    for nom_image in images:
        if nom_image not in cache:          # on génère uniquement si pas déjà en cache
            image_path = os.path.join(app.static_folder, 'images', nom_image)
            cache[nom_image] = generer_histoire(image_path)
            sauvegarder_cache(cache)        # on sauvegarde après chaque image

    return render_template('gallery.html', images=images, histoires=cache)

if __name__ == '__main__':
    app.run(debug=True)