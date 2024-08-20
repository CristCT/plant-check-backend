import tensorflow as tf
import json
from flask import current_app as app

# Ruta del modelo
model_path = app.config['MODEL_PATH']

# Cargar el modelo directamente
model = tf.keras.models.load_model(model_path)

# Cargar las listas desde los archivos JSON
with open(app.config['CLASS_NAMES_FILE'], 'r', encoding='utf-8') as f:
    class_names = json.load(f)

with open(app.config['FRIENDLY_NAMES_FILE'], 'r', encoding='utf-8') as f:
    friendly_names = json.load(f)
