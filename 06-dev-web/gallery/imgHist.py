import ollama
import os

# Chemin vers l'image dans le dossier static de Flask
image_path = os.path.join("static", "images", "closeup-cats.jpg")

response = ollama.chat(
    model="gemma3",
    messages=[
        {
            "role": "user",
            "content": "Regarde cette image et crée une courte histoire pour enfants de 10 phrases. L'histoire doit avoir un héros, une aventure et une fin heureuse.",
            "images": [image_path]
        }
    ]
)

print(response["message"]["content"])