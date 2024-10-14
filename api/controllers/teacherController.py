from api.models.teacherModel import add_teacher_to_db, fetch_all_teachers, fetch_teacher_details, update_teacher_in_db

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
        success, result = fetch_teacher_details(teacher_id)
        return success, result
    except Exception as e:
        print(f"Error in controller while fetching teacher details: {e}")
        return False, "Failed to retrieve teacher details."