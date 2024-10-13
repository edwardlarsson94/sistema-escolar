from database.connection import get_db_connection

def get_students():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT student_id, id_number, first_name, last_name FROM students")
    students = cursor.fetchall()
    connection.close()
    return students

def insert_family_member(family_data):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    sql = """
    INSERT INTO family_members (father_name, mother_name, father_id, mother_id, father_phone, mother_phone, 
                                father_occupation, mother_occupation, father_email, mother_email)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(sql, family_data)
    family_member_id = cursor.lastrowid
    connection.commit()
    connection.close()
    return family_member_id

def insert_representative(representative_data):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    sql = """
    INSERT INTO representatives (rep_name, rep_id, rep_occupation, relationship_to_student, rep_address, 
                                 home_phone, work_phone, cell_phone, rep_email, authorized_person, authorized_person_id)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(sql, representative_data)
    representative_id = cursor.lastrowid
    connection.commit()
    connection.close()
    return representative_id

def insert_student(student_data):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    sql = """
    INSERT INTO students (id_number, first_name, last_name, place_of_birth, nationality, age, birth_day, 
                          birth_month, birth_year, previous_school, has_pending_subjects, pending_subjects, 
                          address, is_repeating, repeating_subjects, lives_with_parents, email, religion, 
                          gender, current_year, phone, family_member_id, representative_id)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(sql, student_data)
    connection.commit()
    connection.close()

def update_student_in_db(student_id, student_data, family_data, representative_data):
    connection = get_db_connection()
    cursor = connection.cursor()

    if not isinstance(student_id, int):
        print(f"Error: student_id debería ser un número entero, pero es '{student_id}'")
        return False, "El ID del estudiante no es válido."

    sql_student = """
    UPDATE students
    SET id_number = ?, first_name = ?, last_name = ?, place_of_birth = ?, nationality = ?, age = ?, 
        birth_day = ?, birth_month = ?, birth_year = ?, previous_school = ?, has_pending_subjects = ?, 
        pending_subjects = ?, address = ?, is_repeating = ?, repeating_subjects = ?, lives_with_parents = ?, 
        email = ?, religion = ?, gender = ?, current_year = ?, phone = ?
    WHERE student_id = ?
    """
    cursor.execute(sql_student, student_data + (student_id,))

    sql_family = """
    UPDATE family_members
    SET father_name = ?, mother_name = ?, father_id = ?, mother_id = ?, father_phone = ?, mother_phone = ?, 
        father_occupation = ?, mother_occupation = ?, father_email = ?, mother_email = ?
    WHERE family_member_id = (SELECT family_member_id FROM students WHERE student_id = ?)
    """
    cursor.execute(sql_family, family_data + (student_id,))

    sql_representative = """
    UPDATE representatives
    SET rep_name = ?, rep_id = ?, rep_occupation = ?, relationship_to_student = ?, rep_address = ?, 
        home_phone = ?, work_phone = ?, cell_phone = ?, rep_email = ?, authorized_person = ?, authorized_person_id = ?
    WHERE representative_id = (SELECT representative_id FROM students WHERE student_id = ?)
    """
    cursor.execute(sql_representative, representative_data + (student_id,))

    connection.commit()
    connection.close()
    return True, "Estudiante actualizado con éxito."

def get_student_details(student_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
    student_data = cursor.fetchone()
    
    cursor.execute("""
        SELECT * FROM family_members 
        WHERE family_member_id = (SELECT family_member_id FROM students WHERE student_id = ?)
    """, (student_id,))
    family_data = cursor.fetchone()
    
    cursor.execute("""
        SELECT * FROM representatives 
        WHERE representative_id = (SELECT representative_id FROM students WHERE student_id = ?)
    """, (student_id,))
    representative_data = cursor.fetchone()
    
    connection.close()
    
    return student_data, family_data, representative_data

def delete_student_from_db(student_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    try:
        cursor.execute("SELECT family_member_id, representative_id FROM students WHERE student_id = ?", (student_id,))
        row = cursor.fetchone()
        
        if row:
            family_member_id, representative_id = row
            
            if family_member_id:
                cursor.execute("DELETE FROM family_members WHERE family_member_id = ?", (family_member_id,))
            
            if representative_id:
                cursor.execute("DELETE FROM representatives WHERE representative_id = ?", (representative_id,))
        
        cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
        
        connection.commit()
        return True, "Estudiante eliminado con éxito."
    
    except Exception as e:
        connection.rollback()
        print(f"Error al eliminar el estudiante y sus datos relacionados: {e}")
        return False, str(e)
    
    finally:
        connection.close()
