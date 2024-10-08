from flask import Flask
from flask_cors import CORS

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app)

    with app.app_context():
        from . import routes

    return app
