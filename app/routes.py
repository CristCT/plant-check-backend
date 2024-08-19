from flask import request, jsonify, current_app as app
from .model import model, class_names, friendly_names
from .utils import preprocess_image
from PIL import Image
import io
import numpy as np

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    img = Image.open(io.BytesIO(file.read()))
    img = preprocess_image(img)
    
    prediction = model.predict(img)
    predicted_class_index = np.argmax(prediction)

    if predicted_class_index >= len(class_names):
        return jsonify({'error': 'Predicted class index out of range'}), 500

    predicted_class_name = class_names[predicted_class_index]
    confidence = prediction[0][predicted_class_index]

    output_type = request.form.get('output_type', 'saludable')

    if output_type == 'saludable':
        result = 'saludable' if 'healthy' in predicted_class_name else 'no saludable'
    elif output_type == 'problemas':
        result = friendly_names.get(predicted_class_name, 'Problema desconocido')

    return jsonify({
        'result': result,
        'confidence': float(confidence)
    })
