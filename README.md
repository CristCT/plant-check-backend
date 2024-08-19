# Plant Check Backend

Este es el backend para la aplicación **Plant Check**, un sistema que utiliza un modelo de TensorFlow para predecir la salud de las hojas. El proyecto está desarrollado en Python utilizando Flask como framework web.

## Características

- **Predicciones de salud de hojas:** El backend recibe imágenes de hojas y utiliza un modelo de TensorFlow para predecir si la hoja está saludable o presenta alguna enfermedad.
- **API REST:** Ofrece una API REST para interactuar con el modelo de predicción.
- **Soporte CORS:** Implementación de CORS para permitir la comunicación con el frontend.

## Estructura del Proyecto

```plaintext
├── app/
│   ├── __init__.py        # Inicializa la aplicación Flask
│   ├── model.py           # Carga del modelo y definición de clases
│   ├── routes.py          # Define las rutas de la API
│   └── utils.py           # Funciones auxiliares para preprocesamiento de imágenes
├── models/                # Directorio con el modelo de TensorFlow (.h5)
├── config.py              # Configuración de la aplicación
├── class_names.json       # Nombres de las clases del modelo
├── friendly_names.json    # Nombres amigables de las clases
├── run.py                 # Script para iniciar la aplicación
├── requirements.txt       # Dependencias del proyecto
└── LICENSE                # Licencia del proyecto
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

### 5. Ejecuta el backend:

```bash
python run.py
```

## Uso de la API

### Endpoint: `/predict`

- **Método:** `POST`
- **Descripción:** Recibe una imagen de una hoja y devuelve la predicción de su salud.
- **Parámetros:** 
  - `file`: Imagen de la hoja (requerido).
  - `output_type`: Tipo de salida (`saludable` o `problemas`). Por defecto es `saludable`.

- **Ejemplo de uso con `curl`:**

```bash
curl -X POST -F 'file=@path_to_image.jpg' -F 'output_type=saludable' http://localhost:5000/predict
```

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
