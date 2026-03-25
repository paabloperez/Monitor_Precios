# notificador.py -> el que se encarga de enviar las notificaciones a Telegram. 
#                   Es el que se encarga de enviar un mensaje cada vez que se detecta un cambio significativo en el precio.
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def enviar_telegram(mensaje):
    token = os.getenv('TELEGRAM_TOKEN')                         # Llave del bot de Telegram
    chat_id = os.getenv('TELEGRAM_CHAT_ID')                     # ID del chat de Telegram al que queremos enviar el mensaje
    url = f"https://api.telegram.org/bot{token}/sendMessage"    # URL de la API de Telegram para enviar mensajes a través del bot
    
    # el payload es el conjunto de datos que le enviamos a Telegram para que sepa a quién enviar el mensaje, qué mensaje enviar y cómo formatearlo. En este caso, le decimos que el mensaje es en formato Markdown para poder usar negritas, emojis, etc.
    payload = {
        'chat_id': chat_id,
        'text': mensaje,
        'parse_mode': 'Markdown'
    }
    
    # En tracker.py hacía GET para obtener el precio, aquí hacemos POST para enviar el mensaje.
    try:
        response = requests.post(url, data=payload) # entrega el mensaje a Telegram
        return response.json()                      # devuelve la respuesta de Telegram en formato JSON, que incluye información sobre si el mensaje se envió correctamente o si hubo algún error.
    except Exception as e:
        print(f"Error al enviar Telegram: {e}")
        return None

if __name__ == "__main__":
    enviar_telegram("🎾 ¡Hola Pablo! Tu monitor de precios está configurado y listo.")