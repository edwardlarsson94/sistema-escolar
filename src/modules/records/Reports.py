import tkinter as tk  # Para la interfaz gráfica
from api.controllers.attendanceController import generate_today_attendance_report
from constants.Colors import BACKGROUND_COLOR, BUTTON_COLOR, BUTTON_TEXT_COLOR, TITLE_COLOR  # Para los colores personalizados
from fpdf import FPDF  # Para crear el PDF
from datetime import datetime 
from tkinter import messagebox 
# Para obtener la fecha actual

def open_reports_window():
    # Crear una nueva ventana para los reportes
    reports_window = tk.Toplevel()
    reports_window.title("Reportes de Docentes")
    reports_window.geometry("400x300")
    reports_window.configure(bg=BACKGROUND_COLOR)

    # Etiqueta de título de la ventana
    label_title = tk.Label(reports_window, text="Reportes de Docentes", bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=("Helvetica", 18, "bold"))
    label_title.pack(pady=20)

    # Aquí puedes agregar el contenido específico para los reportes
    label_info = tk.Label(reports_window, text="Aquí puedes ver y generar reportes", bg=BACKGROUND_COLOR, fg=BUTTON_TEXT_COLOR)
    label_info.pack(pady=10)

    # Botón para generar el reporte
    generate_button = tk.Button(reports_window, text="Generar Reporte de Asistencia", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR,
                                 command=generate_attendance_report)
    generate_button.pack(pady=10)

    # Cerrar ventana
    close_button = tk.Button(reports_window, text="Cerrar", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, command=reports_window.destroy)
    close_button.pack(pady=20)

import datetime
from fpdf import FPDF
from tkinter import messagebox
from api.controllers.attendanceController import generate_today_attendance_report

def generate_attendance_report():
    success, data = generate_today_attendance_report()
    if not success:
        messagebox.showerror("Error", "No se pudo obtener el reporte diario de asistencias.")
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

    pdf.set_font("Arial", size=10)
    for record in data:
        if isinstance(record, dict):
            pdf.cell(col_widths[0], 10, str(record.get("Cédula", "")), 1, 0, 'C')
            pdf.cell(col_widths[1], 10, record.get("Nombre", ""), 1, 0, 'C')
            pdf.cell(col_widths[2], 10, record.get("Apellido", ""), 1, 0, 'C')
            pdf.cell(col_widths[3], 10, record.get("Asignatura", ""), 1, 0, 'C')
            pdf.cell(col_widths[4], 10, record.get("Fecha", ""), 1, 0, 'C')
            pdf.cell(col_widths[5], 10, record.get("Asistencia", ""), 1, 1, 'C')
            print("Formato de datos incorrecto en:", record)

    pdf.output("reporte_asistencias.pdf")

    messagebox.showinfo("Reporte Exitoso", "El reporte de asistencias ha sido generado con éxito.")
