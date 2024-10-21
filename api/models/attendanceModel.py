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

def get_attendances_by_date(selected_date):
    connection = get_db_connection()
    cursor = connection.cursor()
        
    try:
        query = """
        SELECT t.id_number, t.first_name, t.last_name, t.subject, a.status, a.date
        FROM teachers t
        JOIN attendances a ON t.teacher_id = a.teacher_id
        WHERE a.date = ?
        """
        cursor.execute(query, (selected_date,))
        records = cursor.fetchall()
        return True, records
    except Exception as e:
        print(f"Error al obtener asistencias: {e}")
        return False, []
    finally:
        connection.close()
