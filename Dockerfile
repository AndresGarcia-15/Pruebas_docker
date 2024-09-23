# Imagen base de Python
FROM python:3.9-slim

# Configurar directorio de trabajo
WORKDIR /Pruebas_docker

# Copiar archivo requirements.txt y instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Exponer el puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
