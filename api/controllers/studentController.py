from api.models.studentModel import get_students

def get_all_students():
    raw_students = get_students()
    if raw_students:
        student_list = [
            {"id_number": student[0], "first_name": student[1], "last_name": student[2]}
            for student in raw_students
        ]
        return True, student_list
    return False, None