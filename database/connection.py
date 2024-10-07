import sqlite3

def get_db_connection():
    db_path = 'database/sistema_escolar.db'
    connection = sqlite3.connect(db_path)
    return connection
