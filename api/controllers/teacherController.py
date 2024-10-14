from api.models.teacherModel import fetch_all_teachers

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
