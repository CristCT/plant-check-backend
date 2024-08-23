import os
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path=dotenv_path, override=True)

class Config:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    MODEL_PATH_TRADE_OFF = os.path.join(BASE_DIR, '..', 'models', 'model_trade_off.h5')
    MODEL_PATH = os.path.join(BASE_DIR, '..', 'models', 'model.h5')
    CLASS_NAMES_FILE = os.path.join(BASE_DIR, '..', 'class_names.json')
    FRIENDLY_NAMES_FILE = os.path.join(BASE_DIR, '..', 'friendly_names.json')

    DEBUG = False

    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
    DB_NAME = os.getenv('DB_NAME', 'database')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
