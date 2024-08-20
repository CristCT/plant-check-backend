from flask import request, jsonify, current_app as app
from .predict_routes import handle_predict
from .monitor_routes import handle_fetch_monitoreo_plantas

# Ruta para predicciones
@app.route('/predict', methods=['POST'])
def predict():
    return handle_predict()

# Ruta para monitoreo de plantas
@app.route('/monitoreo_plantas', methods=['GET'])
def fetch_monitoreo_plantas():
    return handle_fetch_monitoreo_plantas()
