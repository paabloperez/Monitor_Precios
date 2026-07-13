# 🤖 Monitor de Precios

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-26A5E4?style=flat&logo=telegram&logoColor=white)

Bot autónomo para rastrear el precio de un producto en Tennis-Point y enviar alertas por Telegram cuando el precio baja. Utiliza scraping mediante LD+JSON, almacena el historial en PostgreSQL y corre 24/7 en Docker.

---

## 🚀 Características

- **Scraping con LD+JSON**: extrae datos estructurados de la página para evitar bloqueos y ser robusto a cambios de diseño.
- **Historial de precios**: almacena cada variación en base de datos para análisis futuro.
- **Alertas inteligentes**: solo notifica si el precio baja respecto a la última consulta o cae por debajo del umbral configurado.
- **Dockerizado**: funciona en segundo plano en contenedores aislados.

---

## 🛠️ Requisitos Previos

- [Docker](https://docs.docker.com/get-docker/) y Docker Compose v2.0+
- **Bot de Telegram**: token obtenido vía [@BotFather](https://t.me/botfather)
- **Chat ID**: tu ID de usuario obtenido vía [@userinfobot](https://t.me/userinfobot)

---

## 📦 Instalación

1. **Configurar variables de entorno**:

```bash
cp .env.example .env
```

Edita `.env` con tus valores.

2. **Levantar el sistema**:

```bash
docker compose up -d --build
```

---

## 🕹️ Comandos Útiles

### Gestión de contenedores

| Acción | Comando |
| :--- | :--- |
| Iniciar todo (en segundo plano) | `docker compose up -d` |
| Reconstruir tras cambios | `docker compose up -d --build` |
| Detener el sistema | `docker compose down` |
| Ver estado de contenedores | `docker ps` |

### Logs y depuración

| Acción | Comando |
| :--- | :--- |
| Ver logs del bot en vivo | `docker compose logs -f tennis_bot` |
| Ver logs de la base de datos | `docker compose logs -f monitor_db` |
| Ver últimas 50 líneas | `docker compose logs --tail=50 tennis_bot` |

### Mantenimiento

| Acción | Comando |
| :--- | :--- |
| Limpiar contenedores huérfanos | `docker compose down --remove-orphans` |
| Acceder a la DB (psql) | `docker exec -it monitor_db psql -U $DB_USER -d $DB_NAME` |

---

## 📈 Estructura del Proyecto

```plaintext
Monitor_Precios/
├── bot/
│   ├── main.py          # Bucle de control principal
│   ├── tracker.py       # Lógica de scraping
│   ├── database.py      # Modelos SQLAlchemy y conexión a DB
│   └── notificador.py   # Integración con la API de Telegram
├── docker-compose.yml
└── .env.example
```

---

## ⚖️ Licencia

Proyecto de uso personal y educativo. Respeta siempre los términos de servicio de las webs que rastrees.