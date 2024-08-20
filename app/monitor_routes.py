from flask import jsonify
from .db import get_db_connection

def handle_fetch_monitoreo_plantas():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM monitoreo_plantas WHERE valido=1"
            cursor.execute(sql)
            results = cursor.fetchall()
        return jsonify(results)
    finally:
        connection.close()
