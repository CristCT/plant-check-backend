from flask import current_app as app
from .predict_routes import handle_predict
from .monitor_routes import handle_fetch_camara_data, handle_fetch_invernadero_data, handle_fetch_monitoreo_plantas_data, insert_monitoreo_plantas_data

# Ruta para predicciones
@app.route('/predict', methods=['POST'])
def predict():
    return handle_predict()

# Ruta para monitoreo de plantas
@app.route('/monitoreo_plantas/camara', methods=['GET'])
def fetch_camara_data():
    return handle_fetch_camara_data()

@app.route('/monitoreo_plantas/invernadero', methods=['GET'])
def fetch_invernadero_data():
    return handle_fetch_invernadero_data()

@app.route('/monitoreo_plantas/monitoreo', methods=['GET'])
def fetch_monitoreo_plantas_data():
    return handle_fetch_monitoreo_plantas_data()

# Ruta para guardar resultados de monitoreo de plantas
@app.route('/monitoreo_plantas/guardarResultados', methods=['POST'])
def save_results():
    return insert_monitoreo_plantas_data()

