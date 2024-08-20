import pymysql
from flask import current_app as app

def get_db_connection():
    connection = pymysql.connect(
        host=app.config['DB_HOST'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        db=app.config['DB_NAME'],
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
