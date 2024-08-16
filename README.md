# Plant Check Backend

Este es el backend para la aplicación **Plant Check**, un sistema que utiliza un modelo de TensorFlow para predecir la salud de las hojas de manzana. El proyecto está desarrollado en Python utilizando Flask como framework web.

## Características

- **Predicciones de salud de hojas:** El backend recibe imágenes de hojas de manzana y utiliza un modelo de TensorFlow para predecir si la hoja está saludable o presenta alguna enfermedad.
- **API REST:** Ofrece una API REST para interactuar con el modelo de predicción.
- **Soporte CORS:** Implementación de CORS para permitir la comunicación con el frontend.

## Estructura del Proyecto

```plaintext
├── app/
│   ├── __init__.py        # Inicializa la aplicación Flask
│   ├── model.py           # Carga del modelo y definición de clases
│   ├── routes.py          # Define las rutas de la API
│   └── utils.py           # Funciones auxiliares para preprocesamiento de imágenes
├── .env.example            # Archivo de ejemplo para variables de entorno
├── config.py               # Configuración de la aplicación
├── run.py                  # Script para iniciar la aplicación
├── requirements.txt        # Dependencias del proyecto
└── Procfile                # Archivo para despliegue en Heroku
```

## Requisitos

- Python 3.7 o superior
- Pip (gestor de paquetes de Python)
- Entorno virtual (recomendado)
- TensorFlow y otras dependencias listadas en `requirements.txt`

## Configuración e Instalación

### 1. Clona el repositorio:

```bash
git clone https://github.com/CristCT/plant-check-backend.git
```

### 2. Navega al directorio del proyecto:

```bash
cd plant-check-backend
```

### 3. Crea y activa un entorno virtual (opcional pero recomendado):

- **En Windows:**

  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- **En macOS/Linux:**

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 4. Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

### 5. Configura las variables de entorno:

Crea un archivo `.env` en la raíz del proyecto basado en el archivo `.env.example`. Establece la ruta correcta al modelo de TensorFlow:

```plaintext
MODEL_PATH='./modelo_salud_plantas.h5'
```

### 6. Ejecuta el backend:

```bash
python run.py
```

## Uso de la API

### Endpoint: `/predict`

- **Método:** `POST`
- **Descripción:** Recibe una imagen de una hoja de manzana y devuelve la predicción de su salud.
- **Parámetros:** 
  - `file`: Imagen de la hoja (requerido).
  - `output_type`: Tipo de salida (`saludable` o `problemas`). Por defecto es `saludable`.

- **Ejemplo de uso con `curl`:**

```bash
curl -X POST -F 'file=@path_to_image.jpg' -F 'output_type=saludable' http://localhost:5000/predict
```

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
