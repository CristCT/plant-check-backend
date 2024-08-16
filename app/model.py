import os
import gdown
import tensorflow as tf

# Obtener la URL o el ID del archivo desde las variables de entorno
model_id = os.getenv('GOOGLE_DRIVE_MODEL_ID')
model_url = f'https://drive.google.com/uc?id={model_id}'
model_path = os.getenv('MODEL_PATH', 'models/model.h5')

def download_model():
    if not os.path.exists('models'):
        os.makedirs('models')

    if not os.path.exists(model_path):
        gdown.download(model_url, model_path, quiet=False)

# Descargar el modelo si no existe
download_model()

# Cargar el modelo usando TensorFlow
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
