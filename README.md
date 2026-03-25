---

# 🎾 Monitor de Precios: Head Speed Pro Legend

Este proyecto es un bot autónomo diseñado para rastrear el precio de la raqueta **Head Speed Pro Legend 2025** en Tennis-Point. Utiliza técnicas de web scraping, almacenamiento en base de datos PostgreSQL y notificaciones automáticas vía Telegram.

## 🚀 Características
* **Scraping Inteligente**: Extrae datos estructurados (LD+JSON) para evitar bloqueos y cambios de diseño web.
* **Base de Datos Histórica**: Almacena cada variación de precio para análisis futuro.
* **Alertas Inteligentes**: Solo envía notificaciones a Telegram si el precio baja respecto a la última consulta o baja de un umbral (210€).
* **Dockerizado**: Funciona 24/7 en contenedores aislados.

---

## 🛠️ Requisitos Previos
1. **Docker y Docker Compose** (Versión 2.0+ recomendada).
2. **Bot de Telegram**: Token obtenido vía [@BotFather](https://t.me/botfather).
3. **Chat ID**: Tu ID de usuario obtenido vía [@userinfobot](https://t.me/userinfobot).

---

## 📦 Instalación y Configuración

1. **Configurar variables de entorno**:
   Crea un archivo `.env` en la raíz con el siguiente contenido:
   ```bash
   # Base de Datos (Postgres)
   DB_USER=admin_tennis
   DB_PASSWORD=tu_clave_secreta
   DB_NAME=monitor_precios_db
   DB_HOST=db_monitor
   DB_PORT=5432

   # Telegram
   TELEGRAM_TOKEN=tu_token_de_botfather
   TELEGRAM_CHAT_ID=tu_chat_id
   ```

2. **Levantar el sistema**:
   ```bash
   docker compose up -d --build
   ```

---

## 🕹️ Comandos Importantes (Cheat Sheet)

### Gestión de Contenedores
| Acción | Comando |
| :--- | :--- |
| **Iniciar todo** (en segundo plano) | `docker compose up -d` |
| **Reconstruir tras cambios** | `docker compose up -d --build` |
| **Detener el sistema** | `docker compose down` |
| **Ver estado de contenedores** | `docker ps` |

### Logs y Depuración
| Acción | Comando |
| :--- | :--- |
| **Ver logs del Bot en vivo** | `docker compose logs -f tennis_bot` |
| **Ver logs de la Base de Datos** | `docker compose logs -f monitor_db` |
| **Ver últimas 50 líneas** | `docker compose logs --tail=50 tennis_bot` |

### Mantenimiento
| Acción | Comando |
| :--- | :--- |
| **Limpiar contenedores huérfanos** | `docker compose down --remove-orphans` |
| **Acceder a la DB (psql)** | `docker exec -it monitor_db psql -U admin_tennis -d monitor_precios_db` |

---

## 📈 Estructura del Proyecto
* `/bot`: Código fuente en Python.
    * `tracker.py`: Lógica de Scraping.
    * `database.py`: Modelos de SQLAlchemy y conexión a DB.
    * `notificador.py`: Conexión con la API de Telegram.
    * `main.py`: Cerebro y bucle de control.
* `docker-compose.yml`: Orquestador de los servicios.
* `.env`: Configuración sensible (no subir a repositorios públicos).

---

## ⚖️ Licencia
Este proyecto es de uso personal y educativo. Respeta siempre los términos de servicio de las webs que rastrees.

---