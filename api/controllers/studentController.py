from api.models.studentModel import get_students, insert_family_member, insert_representative, update_student_in_db
from api.models.studentModel import insert_student

def get_all_students():
    raw_students = get_students()
    if raw_students:
        student_list = [
            {"id_number": student[0], "first_name": student[1], "last_name": student[2]}
            for student in raw_students
        ]
        return True, student_list
    return False, None

def add_student_with_relations(student_data, family_data, representative_data):
    try:
        family_member_id = insert_family_member(family_data)
        
        representative_id = insert_representative(representative_data)
        
        student_data_with_ids = student_data + (family_member_id, representative_id)
        
        insert_student(student_data_with_ids)
        
        return True, "Registro exitoso del estudiante y sus datos de relaciones."
    
    except Exception as e:
        print(f"Error al insertar el estudiante con relaciones: {e}")
        return False, f"Error al insertar el estudiante: {e}"

def update_student_with_relations(student_id, student_data, family_data, representative_data):
    try:
        if isinstance(student_id, tuple) and len(student_id) > 0:
            student_id_str = student_id[0]
            student_id = int(''.join(filter(str.isdigit, student_id_str)))
        
        update_student_in_db(student_id, student_data, family_data, representative_data)
        return True, "Estudiante actualizado con éxito"
    except Exception as e:
        return False, str(e)
