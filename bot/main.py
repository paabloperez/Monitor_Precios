# main.py -> el que inicia el monitor, hace el seguimiento del precio, compara con el último precio guardado y decide cuándo enviar notificaciones a Telegram. 
#            Es el corazón del bot, donde se orquesta todo el proceso.
import time
from tracker import rastrear_raqueta
from database import guardar_precio, crear_tablas, SessionLocal, RegistroPrecio
from notificador import enviar_telegram
from sqlalchemy import desc

# Función "Memoria" para obtener el último precio guardado en la base de datos. Antes de decidir si avisarte al móvil, el bot necesita saber qué pasó la última vez.
def obtener_ultimo_precio():
    db = SessionLocal()
    # Buscamos el último registro guardado ordenado por fecha
    ultimo = db.query(RegistroPrecio).order_by(desc(RegistroPrecio.fecha)).first()
    db.close()
    return ultimo.precio if ultimo else None

def iniciar_monitor():
    url = "https://www.tennis-point.es/products/head-speed-pro-legend-2025-raquetas-de-competicion-00607104578000"
    nombre_prod = "Head Speed Pro Legend"
    
    print(f"🚀 Monitor iniciado para: {nombre_prod}")
    crear_tablas()

    while True:
        precio_actual = rastrear_raqueta(url)               # rastrea 
        ultimo_precio_guardado = obtener_ultimo_precio()    # consulta
        
        if precio_actual:                                   # decide
            print(f"🔍 Precio actual: {precio_actual} € | Último en DB: {ultimo_precio_guardado} €")
            
            # 1. Si el precio ha bajado respecto a la última vez que lo vimos
            if ultimo_precio_guardado and precio_actual < ultimo_precio_guardado:
                enviar_telegram(f"📉 ¡BAJADA DE PRECIO! 📉\nLa *{nombre_prod}* ha bajado de {ultimo_precio_guardado}€ a *{precio_actual}€*\n[Correr a la tienda]({url})")
            
            # 2. Si es la primera vez que lo vemos o ha bajado de un umbral fijo (ej. 200€)
            elif precio_actual < 200:
                enviar_telegram(f"🔥 ¡PRECIO CHOLLO! 🔥\nLa {nombre_prod} está a solo *{precio_actual}€*")

            # 3. Guardamos siempre el nuevo precio para tener el histórico
            guardar_precio(nombre_prod, precio_actual)
        
        print("💤 Durmiendo 6 horas...")
        time.sleep(21600) # duerme 6 horas (21600 segundos) antes de volver a revisar el precio

if __name__ == "__main__":
    iniciar_monitor()