import tensorflow as tf
import json
from flask import current_app as app

# Ruta del modelo
model_path_trade_off = app.config['MODEL_PATH_TRADE_OFF']
model_path = app.config['MODEL_PATH']

# Cargar el modelo directamente
model_trade_off = tf.keras.models.load_model(model_path_trade_off)
model = tf.keras.models.load_model(model_path)

# Cargar las listas desde los archivos JSON
with open(app.config['CLASS_NAMES_FILE'], 'r', encoding='utf-8') as f:
    class_names = json.load(f)

with open(app.config['FRIENDLY_NAMES_FILE'], 'r', encoding='utf-8') as f:
    friendly_names = json.load(f)
