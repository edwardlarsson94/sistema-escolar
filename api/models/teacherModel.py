from database.connection import get_db_connection

def fetch_all_teachers():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    query = "SELECT teacher_id, id_number, first_name, subject, phone FROM teachers"
    cursor.execute(query)
    teachers = cursor.fetchall()
    connection.close()

    return teachers

def add_teacher_to_db(id_number, first_name, last_name, age, sex, address, subject, phone):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    query = """
    INSERT INTO teachers (id_number, first_name, last_name, age, sex, address, subject, phone)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    try:
        cursor.execute(query, (id_number, first_name, last_name, age, sex, address, subject, phone))
        connection.commit()
        return True, "Teacher added successfully."
    except Exception as e:
        print(f"Error adding teacher to the database: {e}")
        return False, "Failed to add teacher."
    finally:
        connection.close()

def update_teacher_in_db(teacher_id, id_number, first_name, last_name, age, sex, address, subject, phone):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    query = """
    UPDATE teachers
    SET id_number = ?, first_name = ?, last_name = ?, age = ?, sex = ?, address = ?, subject = ?, phone = ?
    WHERE teacher_id = ?
    """
    try:
        cursor.execute(query, (id_number, first_name, last_name, age, sex, address, subject, phone, teacher_id))
        connection.commit()
        return True, "Teacher updated successfully."
    except Exception as e:
        print(f"Error updating teacher: {e}")
        return False, "Failed to update teacher."
    finally:
        connection.close()

def fetch_teacher_details(teacher_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    query = "SELECT id_number, first_name, last_name, age, sex, address, subject, phone FROM teachers WHERE teacher_id = ?"
    try:
        cursor.execute(query, (teacher_id,))
        teacher = cursor.fetchone()
        return teacher
    except Exception as e:
        print(f"Error fetching teacher details: {e}")
        return None
    finally:
        connection.close()