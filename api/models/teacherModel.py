from database.connection import get_db_connection

def fetch_all_teachers():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    query = "SELECT teacher_id, id_number, first_name, subject, phone FROM teachers"
    cursor.execute(query)
    teachers = cursor.fetchall()
    connection.close()

    return teachers
