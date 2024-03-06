# Usa una imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY agify_api.py .
COPY genderize_api.py .
COPY uso_agify.py .
COPY uso_genderize.py .
COPY uso_apis.py .
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 5000 para que puedas acceder al servidor Flask
EXPOSE 5000

# Comando para ejecutar el servidor Flask al iniciar el contenedor
CMD ["python", "uso_apis.py"]
