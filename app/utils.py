from PIL import Image
import numpy as np

def preprocess_image(image):
    # Redimensionar la imagen
    image = image.resize((256, 256))

    # Convertir a RGB si la imagen tiene un canal alfa
    if image.mode == 'RGBA':
        image = image.convert('RGB')

    # Convertir a array numpy y normalizar
    image_array = np.array(image) / 255.0

    # Asegurarse de que la imagen tenga 3 canales
    if len(image_array.shape) == 2:  # Imagen en escala de grises
        image_array = np.stack((image_array,) * 3, axis=-1)
    elif image_array.shape[2] == 4:  # Imagen con canal alfa
        image_array = image_array[:, :, :3]

    # Añadir dimensión de lote
    image_array = np.expand_dims(image_array, axis=0)
    
    # Verificar la forma final
    assert image_array.shape == (1, 256, 256, 3), f"Forma incorrecta: {image_array.shape}"
    
    return image_array