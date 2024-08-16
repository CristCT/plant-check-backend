from PIL import Image
import numpy as np

def preprocess_image(image):
    image = image.resize((256, 256))  # Tamaño esperado por el modelo
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image
