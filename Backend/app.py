from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)

# Liste des challenges (à compléter plus tard)
CHALLENGES = {
    "bank_heist": {"description": "Hack the bank using JWT vulnerabilities.", "port": 3001},
    "picky_website": {"description": "Find the hidden flag using HTTP headers.", "port": 3002},
    "forensic": {"description": "Analyze network packets to reconstruct the flag.", "port": 3003},
    "web_ctf": {"description": "Solve the Web CTF challenge.", "port": 3004}
}

@app.route('/challenges', methods=['GET'])
def get_challenges():
    """Retourne la liste des défis."""
    return jsonify({"challenges": CHALLENGES})

@app.route('/start_challenge/<challenge_name>', methods=['POST'])
def start_challenge(challenge_name):
    """Démarre un défi spécifique."""
    challenge = CHALLENGES.get(challenge_name)
    if not challenge:
        return jsonify({"error": "Challenge not found"}), 404

    try:
        # Simule le démarrage d'un défi
        return jsonify({"message": f"Challenge {challenge_name} started on port {challenge['port']}!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/stop_all', methods=['POST'])
def stop_all():
    """Arrête tous les défis."""
    try:
        # Simule l'arrêt de tous les défis
        return jsonify({"message": "All challenges stopped!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
