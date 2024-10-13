from database.connection import get_db_connection

def get_students():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id_number, first_name, last_name FROM students")
    students = cursor.fetchall()
    connection.close()
    return students
