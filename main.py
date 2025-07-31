from flask import Flask, request
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/TON_WEBHOOK"

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    content = data.get("content", "")
    if content:
        requests.post(WEBHOOK_URL, json={"content": content})
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)