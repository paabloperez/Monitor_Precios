# Usamos una versión ligera de Python
FROM python:3.10-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app
ENV PYTHONUNBUFFERED=1

# Instalamos las librerías necesarias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código del bot
COPY . .

# Comando para arrancar el monitor
CMD ["python", "main.py"]