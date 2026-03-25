# tracker.py -> es el que sale a internet a buscar el dato del precio de la raqueta.
#               Es el que se encarga de hacer el web scraping y devolver el precio actual. Si no encuentra el precio, devuelve None.

import requests                 # Es la librería que usaremos para hacer las peticiones HTTP a la página web. Nos trae el contenido HTML de la página.
from bs4 import BeautifulSoup   # Es la librería que usaremos para analizar el contenido HTML y extraer el precio. Nos permite navegar por la estructura del HTML de forma sencilla.
import json                     # Es la librería que usaremos para manejar los datos en formato JSON, especialmente para analizar los datos estructurados (LD+JSON) que muchas páginas incluyen para SEO.

def rastrear_raqueta(url):
    
    headers = {              
        # Es importante usar un User-Agent para que la página no nos bloquee por ser un bot. Simulamos ser un navegador común.   
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    def limpiar_precio(valor):
        # Esta función convierte el precio que puede venir en formato '204,95' o '204.95' a un float válido. Reemplaza la coma por punto y luego intenta convertirlo a float. Si no se puede convertir, devuelve None.
        try:
            return float(str(valor).replace(',', '.'))
        except (ValueError, TypeError):
            return None

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 1. Buscar en LD+JSON (Datos estructurados)
        scripts = soup.find_all('script', type='application/ld+json')
        for script in scripts:
            try:
                data = json.loads(script.string)
                
                # Caso A: El JSON es un diccionario directo
                if isinstance(data, dict):
                    if 'offers' in data:
                        oferta = data['offers']
                        if isinstance(oferta, list): oferta = oferta[0]
                        return limpiar_precio(oferta.get('price'))
                    # A veces el precio está en 'mainEntity'
                    if 'mainEntity' in data and 'offers' in data['mainEntity']:
                        oferta = data['mainEntity']['offers']
                        if isinstance(oferta, list): oferta = oferta[0]
                        return limpiar_precio(oferta.get('price'))

                # Caso B: El JSON es una lista de objetos
                elif isinstance(data, list):
                    for item in data:
                        if 'offers' in item:
                            oferta = item['offers']
                            if isinstance(oferta, list): oferta = oferta[0]
                            return limpiar_precio(oferta.get('price'))
            except:
                continue

        # 2. Plan B: Meta etiquetas (OpenGraph)
        meta_precio = soup.find("meta", property="product:price:amount") or \
                      soup.find("meta", property="og:price:amount")
        if meta_precio:
            return limpiar_precio(meta_precio["content"])

    # Si no encontramos el precio, devolvemos None
    except Exception as e:
        print(f"Error: {e}")
    return None

url_head = "https://www.tennis-point.es/products/head-speed-pro-legend-2025-raquetas-de-competicion-00607104578000"
precio = rastrear_raqueta(url_head)

if precio:
    print(f"✅ ¡ÉXITO! El precio de la Head Speed Pro Legend es: {precio} €")
else:
    print("❌ Seguimos sin encontrarlo. La web se resiste.")