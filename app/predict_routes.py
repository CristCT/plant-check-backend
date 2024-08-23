from flask import request, jsonify, current_app as app
from .model import model, model_trade_off, class_names, friendly_names
from .utils import preprocess_image
from PIL import Image
import io
import numpy as np

def handle_predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    img = Image.open(io.BytesIO(file.read()))
    img = preprocess_image(img)
    
    use_trade_off_model = request.form.get('use_trade_off_model', 'true').lower() == 'true'
    
    if use_trade_off_model:
        selected_model = model_trade_off
    else:
        selected_model = model
    
    # Realizar la predicción usando el modelo seleccionado
    prediction = selected_model.predict(img)
    
    # Obtener los 5 mejores resultados
    top_5_indices = np.argsort(prediction[0])[-5:][::-1]
    top_5_predictions = [
        {"class": class_names[i], "probability": float(prediction[0][i])}
        for i in top_5_indices
    ]
    
    output_type = request.form.get('output_type', 'saludable')
    
    # Encontrar la predicción saludable y no saludable más probable
    healthy_prediction = next((pred for pred in top_5_predictions if 'healthy' in pred['class']), None)
    unhealthy_prediction = next((pred for pred in top_5_predictions if 'healthy' not in pred['class']), None)
    
    if output_type == 'saludable':
        if healthy_prediction and healthy_prediction['probability'] > 0.9:
            result = 'Saludable'
            confidence = healthy_prediction['probability']
        elif healthy_prediction:
            result = f"Mayormente saludable, pero con signos de {friendly_names.get(unhealthy_prediction['class'], 'problema desconocido')}"
            confidence = healthy_prediction['probability']
        else:
            result = 'Planta no saludable'
            confidence = unhealthy_prediction['probability'] if unhealthy_prediction else 0.0
    
    elif output_type == 'problemas':
        if unhealthy_prediction and unhealthy_prediction['probability'] > 0.5:
            result = friendly_names.get(unhealthy_prediction['class'], 'Problema desconocido')
            confidence = unhealthy_prediction['probability']
        elif unhealthy_prediction:
            result = f"Signos leves de {friendly_names.get(unhealthy_prediction['class'], 'problema desconocido')}"
            confidence = unhealthy_prediction['probability']
        else:
            result = 'No se detectaron problemas significativos'
            confidence = healthy_prediction['probability'] if healthy_prediction else 1.0
    
    else:
        return jsonify({'error': 'Invalid output_type'}), 400

    return jsonify({
        'result': result,
        'confidence': confidence,
        'predictions': top_5_predictions
    })
