from flask import jsonify
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
