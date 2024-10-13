from database.connection import get_db_connection

def get_students():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id_number, first_name, last_name FROM students")
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
