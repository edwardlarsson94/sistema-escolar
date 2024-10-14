from api.models.studentModel import insert_student, delete_student_from_db, get_student_details, get_students, insert_family_member, insert_representative, update_student_in_db

def get_all_students():
    raw_students = get_students()
    if raw_students:
        student_list = [
            {
                'student_id': student[0],
                'id_number': student[1],
                'first_name': student[2],
                'last_name': student[3]
            }
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
            student_id = student_id[0]
        
        if isinstance(student_id, str):
            student_id = int(''.join(filter(str.isdigit, student_id)))
        elif not isinstance(student_id, int):
            raise ValueError("El ID del estudiante no es válido")

        update_student_in_db(student_id, student_data, family_data, representative_data)
        return True, "Estudiante actualizado con éxito"
    except Exception as e:
        return False, str(e)

def fetch_student_details(student_id):
    try:
        if isinstance(student_id, tuple) and len(student_id) > 0:
            student_id_str = student_id[0]
            student_id = int(''.join(filter(str.isdigit, student_id_str)))

        student_data, family_data, representative_data = get_student_details(student_id)
        return student_data, family_data, representative_data
    except Exception as e:
        print(f"Error al obtener los detalles del estudiante: {e}")
        return None, None, None
    
def delete_student(student_id):
    print(f"Eliminando estudiante con ID {student_id}")
    try:
        success, message = delete_student_from_db(student_id)
        return success, message
    except Exception as e:
        print(f"Error al eliminar los datos del estudiante: {e}")
        return False, f"Error: {str(e)}"