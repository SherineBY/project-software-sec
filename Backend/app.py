import os
from flask import Flask, send_from_directory

# Initialisation de l'application Flask
app = Flask(__name__, static_folder="Frontend/assets", static_url_path="/assets")

@app.route('/')
def home():
    """
    Sert le fichier index.html depuis le dossier Frontend.
    """
    frontend_path = os.path.abspath("Frontend")  # Chemin absolu vers Frontend
    print(f"Serving index.html from {frontend_path}")
    return send_from_directory(frontend_path, 'index.html')

@app.route('/assets/<path:filename>')
def static_files(filename):
    """
    Sert les fichiers statiques (CSS, JS, images) depuis Frontend/assets.
    """
    assets_path = os.path.abspath("Frontend/assets")  # Chemin absolu vers les assets
    print(f"Serving static file: {filename} from {assets_path}")
    return send_from_directory(assets_path, filename)

@app.route('/challenges/<path:filename>')
def serve_challenges(filename):
    """
    Sert les fichiers des challenges depuis le dossier Challenges.
    """
    challenges_path = os.path.abspath("Challenges")  # Chemin absolu vers Challenges
    print(f"Serving challenge file: {filename} from {challenges_path}")
    return send_from_directory(challenges_path, filename)

if __name__ == '__main__':
    # Lancer le serveur Flask
    app.run(debug=True, host='0.0.0.0', port=5000)
