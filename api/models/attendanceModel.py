from database.connection import get_db_connection

def add_attendance(teacher_id, date, status):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    try:
        query = "INSERT INTO attendances (teacher_id, date, status) VALUES (?, ?, ?)"
        cursor.execute(query, (teacher_id, date, status))
        connection.commit()
        return True, "Asistencia registrada correctamente."
    except Exception as e:
        print(f"Error al registrar asistencia: {e}")
        return False, "No se pudo registrar la asistencia."
    finally:
        connection.close()
