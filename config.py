import os

class Config:
    MODEL_PATH = os.getenv('MODEL_PATH')

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': Config,
    'production': ProductionConfig
}
