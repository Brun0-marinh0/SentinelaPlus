import requests

from dotenv import load_dotenv
import os

load_dotenv()

def send_telegram(message: str):
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "MarkdownV2"
    }

    try:
        response = requests.post(url, data=data, timeout=20)
        if response.status_code != 200:
            print(f"💬✖ Falha ao enviar mensagem Telegram: {response.text}")
    except Exception as err:
        print(f"💬❌ Erro no envio Telegram: {err}")