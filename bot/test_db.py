from database import crear_tablas, guardar_precio

# 1. Crea la tabla si no existe
print("Creando tablas...")
crear_tablas()

# 2. Intenta guardar un precio de prueba
print("Guardando precio de prueba...")
guardar_precio("Head Speed Pro Legend", 204.95)

print("✅ ¡Conexión y guardado exitosos!")