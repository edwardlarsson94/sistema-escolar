from api.models.attendanceModel import add_attendance
from datetime import datetime

def register_teacher_attendance(teacher_id, status):
    date = datetime.now().strftime("%Y-%m-%d")
    success, message = add_attendance(teacher_id, date, status)
    return success, message
