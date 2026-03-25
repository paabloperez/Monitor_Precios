import os
import requests
from dotenv import load_dotenv

load_dotenv()

def enviar_telegram(mensaje):
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    payload = {
        'chat_id': chat_id,
        'text': mensaje,
        'parse_mode': 'Markdown'
    }
    
    try:
        response = requests.post(url, data=payload)
        return response.json()
    except Exception as e:
        print(f"Error al enviar Telegram: {e}")
        return None

if __name__ == "__main__":
    enviar_telegram("🎾 ¡Hola Pablo! Tu monitor de precios está configurado y listo.")