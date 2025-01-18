from flask import Flask, render_template, request, redirect, url_for
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



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/start/middle-picky', methods=['GET'])
def start_picky_challenge():
    # Redirige directement vers le port 3000 sans lancer Docker
    return redirect("http://localhost:3000")



@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
