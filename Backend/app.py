from flask import Flask, render_template, request, redirect, url_for, send_from_directory, abort, send_file
import os
import subprocess

app = Flask(__name__, template_folder="templates")

CHALLENGE_PATHS = {
    "hard-network": "Challenges/Hard_Challenge-Network/Hard_Challenge-Network",
    "hard-forensic": "Challenges/Hard-Challenge-Forensic",
    "middle-picky": "Challenges/Middle-Challenge-Web",
    "middle-desc": "Challenges/Middle-Challenge"
}

PICKY_WEBSITE_PATH = os.path.abspath("Challenges/Middle-Challenge-Web/picky-website")

DOCKER_COMMANDS = {
    "hard-network": "docker run -d -p 3001:5000 --name hard-network my-image",
    "hard-forensic": "docker run -d -p 3002:5000 --name hard-forensic my-image",
    "middle-picky": f"docker run -d -p 3000:3000 --name picky-website -v {PICKY_WEBSITE_PATH}",
    "middle-desc": "docker run -d -p 3004:5000 --name middle-desc my-image"
}

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHALLENGE_SCRIPT = os.path.join(BASE_DIR, "Challenges", "Hard-Chanllenge-Forensic", "Hard-Chanllenge-Forensic", "challenge.py")

print("Chemin complet vers challenge.py :", CHALLENGE_SCRIPT)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/start/hard-forensic', methods=['POST'])
def start_hard_forensic():
    try:
        # Chemin absolu vers challenge.py
        script_path = r"C:\Users\sheri\Documents\GitHub\project-software-sec\Challenges\Hard-Chanllenge-Forensic\Hard-Chanllenge-Forensic\challenge.py"
        
        # Commande pour exécuter le script
        command = ["python", script_path]
        
        # Exécution du script
        subprocess.run(command, check=True)
        
        # Une fois terminé, redirection ou message de succès
        return "Challenge lancé avec succès ! Le fichier 'challenge.png' a été généré.", 200
    except subprocess.CalledProcessError as e:
        return f"Erreur lors du lancement du challenge : {e}", 500
    
FORENSIC_PATH = os.path.abspath(
    "Challenges/Hard-Chanllenge-Forensic/Hard-Chanllenge-Forensic")
   
@app.route("/Challenges/Hard-Chanllenge-Forensic/<filename>")
def serve_forensic_file(filename):
    try:
        # Sert les fichiers présents dans le dossier FORENSIC_PATH
        return send_from_directory(FORENSIC_PATH, filename)
    except FileNotFoundError:
        return "Fichier introuvable.", 404
    
@app.route('/forensic-description', methods=['GET'])
def forensic_description():
    # Rendu direct du fichier HTML via Flask
    return render_template('Forensic_description.html')

@app.route('/download/hard-challenge-network', methods=['GET'])
def download_hard_challenge():
    # Chemin absolu du fichier zip
    zip_path = r"C:\Users\sheri\Documents\GitHub\project-software-sec\Challenges\Hard_Challenge-Network.zip"
    try:
        return send_file(zip_path, as_attachment=True)
    except FileNotFoundError:
        return "Le fichier n'existe pas.", 404


@app.route("/network-solution", methods=['GET'])
def network_solution():
    try:
        # Sert le fichier "Detailed-Solution.pdf" depuis le dossier "templates"
        return send_from_directory(directory="templates", filename="Detailed-Solution.pdf")
    except FileNotFoundError:
        return "Le fichier Detailed-Solution.pdf est introuvable.", 404  

#medium challenges       
@app.route('/start/middle-picky', methods=['GET'])
def start_picky_challenge():
    # Redirige directement vers le port 3000 sans lancer Docker
    return redirect("http://localhost:3000")


@app.route('/picky-description', methods=['GET'])
def picky_description():
    # Rendu direct du fichier HTML via Flask
    return render_template('picky_website_medium.html')

WEB_CTF_PATH = "C:/Users/sheri/Documents/GitHub/project-software-sec/Challenges/Middle-Challenge/Middle-Challenge/webCTF.py"
MIDDLE_CHALLENGE_PATH = "C:/Users/sheri/Documents/GitHub/project-software-sec/Challenges/Middle-Challenge/Middle-Challenge"

@app.route('/web-ctf-challenge')
def serve_web_ctf():
    try:
        # Sert le fichier CTFchallenge.html
        return send_from_directory(
            directory=MIDDLE_CHALLENGE_PATH,
            filename="CTFchallenge.html"
        )
    except FileNotFoundError:
        return "Le fichier CTFchallenge.html n'a pas été trouvé.", 404
    
import subprocess

WEB_CTF_PATH = "C:/Users/sheri/Documents/GitHub/project-software-sec/Challenges/Middle-Challenge/Middle-Challenge/webCTF.py"

@app.route('/start/web-ctf', methods=['POST'])
def start_web_ctf():
    try:
        # Exécute le script webCTF.py
        subprocess.run(["python", WEB_CTF_PATH], check=True)

        # Redirige vers la route qui sert le fichier
        return redirect("/web-ctf-challenge")
    except subprocess.CalledProcessError as e:
        return f"Erreur lors du lancement du challenge Web CTF : {e}", 500

@app.route('/ctf-description', methods=['GET'])
def ctf_description():
    # Rendu direct du fichier HTML via Flask
    return render_template('CTF_description.html')

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404

@app.route("/ctf-solution", methods=['GET'])
def ctf_solution():
    return render_template("CTF_solution.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
