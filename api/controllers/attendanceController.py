from api.models.attendanceModel import add_attendance, get_today_attendances
from datetime import datetime

def register_teacher_attendance(teacher_id, status):
    date = datetime.now().strftime("%Y-%m-%d")
    success, message = add_attendance(teacher_id, date, status)
    return success, message

def generate_today_attendance_report():
    today = datetime.now().strftime("%Y-%m-%d")
    success, records = get_today_attendances(today)
    
    if success:
        report_data = []
        
        for record in records:
            id_number, first_name, last_name, subject, status, date = record
            report_data.append({
                "Cédula": id_number,
                "Nombre": first_name,
                "Apellido": last_name,
                "Asignatura": subject,
                "Fecha": date,
                "Asistencia": status
            })
        
        return True, report_data
    else:
        return False, "No se pudo generar el reporte de asistencia."