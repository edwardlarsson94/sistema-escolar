from api.models.teacherModel import add_teacher_to_db, delete_teacher_by_id, fetch_all_teachers, fetch_teacher_details, update_teacher_in_db

def get_all_teachers():
    try:
        teachers_data = fetch_all_teachers()

        teacher_list = [
            {
                "teacher_id": teacher[0],
                "id_number": teacher[1],
                "first_name": teacher[2],
                "subject": teacher[3],
                "phone": teacher[4]
            }
            for teacher in teachers_data
        ]
        
        return True, teacher_list
    except Exception as e:
        print(f"Error al obtener los datos de los profesores: {e}")
        return False, []

def add_teacher_new(id_number, first_name, last_name, age, sex, address, subject, phone):
    try:
        success, message = add_teacher_to_db(id_number, first_name, last_name, age, sex, address, subject, phone)
        return success, message
    except Exception as e:
        print(f"Error while adding teacher: {e}")
        return False, "Failed to add teacher."

def update_teacher_by_id(teacher_id, id_number, first_name, last_name, age, sex, address, subject, phone):
    try:
        success, message = update_teacher_in_db(teacher_id, id_number, first_name, last_name, age, sex, address, subject, phone)
        return success, message
    except Exception as e:
        print(f"Error while updating teacher: {e}")
        return False, "Failed to update teacher."

def get_teacher_details(teacher_id):
    try:
        teacher = fetch_teacher_details(teacher_id)
        
        if teacher:
            teacher_data = {
                "id_number": teacher[0],
                "first_name": teacher[1],
                "last_name": teacher[2],
                "age": teacher[3],
                "sex": teacher[4],
                "address": teacher[5],
                "subject": teacher[6],
                "phone": teacher[7]
            }
            return True, teacher_data
        else:
            return False, "Teacher not found."
    except Exception as e:
        print(f"Error in controller while fetching teacher details: {e}")
        return False, "Failed to retrieve teacher details."
    
def remove_teacher(teacher_id):
    success, message = delete_teacher_by_id(teacher_id)
    return success, message
