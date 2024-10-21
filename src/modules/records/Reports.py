import datetime
from fpdf import FPDF
from tkinter import messagebox
from api.controllers.attendanceController import generate_today_attendance_report

def generate_attendance_report():
    success, data = generate_today_attendance_report()
    
    # Verificar si hay éxito en la obtención del reporte
    if not success:
        messagebox.showerror("Error", "No se pudo obtener el reporte diario de asistencias.")
        return

    # Verificar si los datos tienen el formato correcto (una lista de diccionarios)
    if not isinstance(data, list) or not all(isinstance(record, dict) for record in data):
        messagebox.showerror("Error", "El formato de los datos de asistencia no es válido.")
        return
    
    # Verificar si hay datos para generar el reporte
    if len(data) == 0:
        messagebox.showerror("Error", "No hay datos de asistencia para el día de hoy.")
        return

    # Crear PDF
    pdf = FPDF(orientation='L')  # 'L' para landscape (horizontal)
    pdf.add_page()

    # Título del reporte
    pdf.set_font("Arial", size=12)
    pdf.cell(250, 10, txt="Reportes de Asistencias del Día", ln=True, align='C')

    # Espacio antes de la tabla
    pdf.ln(10)

    # Definir ancho de las columnas
    col_widths = [30, 40, 40, 50, 50, 40]  # Ajusta los valores según sea necesario

    # Calcular el ancho total de la tabla
    table_width = sum(col_widths)

    # Obtener el ancho de la página
    page_width = pdf.w - 2 * pdf.l_margin

    # Aumentar aún más el margen izquierdo para mover la tabla más a la derecha
    left_margin = (page_width - table_width) / 1.5  # Movemos más a la derecha

    # Aplicar el margen izquierdo calculado
    pdf.set_left_margin(left_margin)
    pdf.set_x(left_margin)

    # Crear la cabecera de la tabla
    pdf.set_font("Arial", size=10, style='B')
    headers = ["Cédula", "Nombre", "Apellido", "Asignatura", "Fecha Actual", "Asistencia"]
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 10, header, 1, 0, 'C')
    pdf.ln(10)

    # Escribir los registros de asistencia
    pdf.set_font("Arial", size=10)
    for record in data:
        try:
            pdf.cell(col_widths[0], 10, str(record.get("Cédula", "N/A")), 1, 0, 'C')
            pdf.cell(col_widths[1], 10, record.get("Nombre", "N/A"), 1, 0, 'C')
            pdf.cell(col_widths[2], 10, record.get("Apellido", "N/A"), 1, 0, 'C')
            pdf.cell(col_widths[3], 10, record.get("Asignatura", "N/A"), 1, 0, 'C')
            pdf.cell(col_widths[4], 10, record.get("Fecha", "N/A"), 1, 0, 'C')
            pdf.cell(col_widths[5], 10, record.get("Asistencia", "N/A"), 1, 1, 'C')
        except KeyError as e:
            print(f"Error: Falta la clave {e} en el registro: {record}")

    # Guardar el PDF
    pdf.output("reporte_asistencias.pdf")

    # Confirmación al usuario
    messagebox.showinfo("Reporte Exitoso", "El reporte de asistencias ha sido generado con éxito.")
