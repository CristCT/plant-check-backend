import os

class Config:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    MODEL_PATH = os.path.join(BASE_DIR, 'models', 'model.h5')
    CLASS_NAMES_FILE = os.path.join(BASE_DIR, 'class_names.json')
    FRIENDLY_NAMES_FILE = os.path.join(BASE_DIR, 'friendly_names.json')

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': Config,
    'production': ProductionConfig
}
