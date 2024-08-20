import tensorflow as tf
import json
from app.config import Config

# Ruta del modelo
model_path = Config.MODEL_PATH

# Cargar el modelo directamente
model = tf.keras.models.load_model(model_path)

# Cargar las listas desde los archivos JSON
with open(Config.CLASS_NAMES_FILE, 'r', encoding='utf-8') as f:
    class_names = json.load(f)

with open(Config.FRIENDLY_NAMES_FILE, 'r', encoding='utf-8') as f:
    friendly_names = json.load(f)
