import os
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Cargamos las variables del .env
load_dotenv()

# Configuración de la URL de la base de datos (usando las variables del .env)
# Formato: postgresql://usuario:password@host:puerto/nombre_db
DB_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT', '5432')}/{os.getenv('DB_NAME')}"
# El "Engine" es el motor de conexión
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- MODELO DE LA TABLA ---
class RegistroPrecio(Base):
    __tablename__ = "precios_historico"

    id = Column(Integer, primary_key=True, index=True)
    nombre_producto = Column(String)
    precio = Column(Float)
    fecha = Column(DateTime, default=datetime.utcnow)

# Función para crear las tablas en la base de datos
def crear_tablas():
    Base.metadata.create_all(bind=engine)

# Función para guardar un nuevo precio
def guardar_precio(nombre, valor):
    db = SessionLocal()
    nuevo_registro = RegistroPrecio(nombre_producto=nombre, precio=valor)
    db.add(nuevo_registro)
    db.commit()
    db.refresh(nuevo_registro)
    db.close()
    return nuevo_registro