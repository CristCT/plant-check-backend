import tensorflow as tf
import os

# Cargar el modelo usando la variable de entorno
model_path = os.getenv('MODEL_PATH', 'default/path/to/model.h5')
model = tf.keras.models.load_model(model_path)

class_names = [
    'Apple___healthy',
    'Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust'
]

friendly_names = {
    'Apple___healthy': 'saludable',
    'Apple___Apple_scab': 'Manchas en la hoja',
    'Apple___Black_rot': 'Podredumbre negra',
    'Apple___Cedar_apple_rust': 'Roya del manzano'
}
