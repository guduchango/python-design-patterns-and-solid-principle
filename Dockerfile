FROM python:3.11-slim

# Configura el directorio de trabajo
WORKDIR /app

# Instala dependencias
COPY app/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir debugpy

# Copia el código fuente
COPY app /app

# Expone el puerto para el depurador
EXPOSE 5678

# Comando por defecto para iniciar la app
CMD ["python", "main.py"]
