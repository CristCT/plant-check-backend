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
