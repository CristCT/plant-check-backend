from flask import request, jsonify
from datetime import datetime
from .db import get_db_connection

def fetch_data_from_table(table_name):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("USE monitoreo_plantas;")
            cursor.execute(f"SELECT * FROM {table_name};")
            results = cursor.fetchall()

            # Convertir bytes a string si es necesario
            converted_results = []
            for row in results:
                converted_row = {key: (value.decode('utf-8') if isinstance(value, bytes) else value) for key, value in row.items()}
                converted_results.append(converted_row)
                
        return jsonify(converted_results)
    finally:
        connection.close()

def handle_fetch_camara_data():
    return fetch_data_from_table('camara')

def handle_fetch_invernadero_data():
    return fetch_data_from_table('invernadero')

def handle_fetch_monitoreo_plantas_data():
    return fetch_data_from_table('monitoreo_plantas')

def insert_monitoreo_plantas_data():
    connection = get_db_connection()
    try:
        data = request.get_json()

        if not isinstance(data, list):
            return jsonify({'error': 'Los datos enviados no son una lista'}), 400

        with connection.cursor() as cursor:
            for result in data:
                idcamara = result.get('idcamara')
                resultado_modelo = result.get('resultado_modelo')
                planta = result.get('planta')
                healthy = result.get('healthy')
                time_str = result.get('time')
                fecha_registro_str = result.get('fecha_registro')
                valido = result.get('valido', True)

                time = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S.%fZ").strftime('%Y-%m-%d %H:%M:%S')
                fecha_registro = datetime.strptime(fecha_registro_str, "%Y-%m-%dT%H:%M:%S.%fZ").strftime('%Y-%m-%d %H:%M:%S')

                cursor.execute("""
                    INSERT INTO monitoreo_plantas (idcamara, resultado_modelo, planta, healthy, time, fecha_registro, valido)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (idcamara, resultado_modelo, planta, healthy, time, fecha_registro, valido))

            connection.commit()

        return jsonify({"message": "Resultados guardados exitosamente"}), 201
    except Exception as e:
        connection.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()
