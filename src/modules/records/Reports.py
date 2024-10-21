import tkinter as tk
from tkinter import messagebox
from fpdf import FPDF
from api.controllers.attendanceController import generate_attendance_report_by_date
import datetime

from constants.Colors import BACKGROUND_COLOR, BUTTON_COLOR, BUTTON_TEXT_COLOR, ENTRY_BACKGROUND, ENTRY_FOREGROUND, TITLE_COLOR

# Función para abrir la ventana de reportes
def open_reports_window():
    # Crear la ventana de reportes
    reports_window = tk.Toplevel()
    reports_window.title("Generar Reporte de Asistencia")
    reports_window.geometry("400x300")
    reports_window.configure(bg=BACKGROUND_COLOR)

    # Título de la ventana
    label_title = tk.Label(reports_window, text="Generar Reporte de Asistencia", bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=("Helvetica", 18, "bold"))
    label_title.pack(pady=20)

    # Campo de fecha
    label_date = tk.Label(reports_window, text="Ingrese la fecha (YYYY-MM-DD):", bg=BACKGROUND_COLOR, fg=BUTTON_TEXT_COLOR)
    label_date.pack(pady=5)

    date_entry = tk.Entry(reports_window, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND)
    date_entry.pack(pady=5)

    # Botón para generar el reporte, pasando el valor del campo de fecha
    generate_button = tk.Button(reports_window, text="Generar Reporte", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR,
                                command=lambda: generate_attendance_report(date_entry.get()))  # Se pasa el valor de la fecha ingresada
    generate_button.pack(pady=10)

    # Botón para cerrar la ventana
    close_button = tk.Button(reports_window, text="Cerrar", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, command=reports_window.destroy)
    close_button.pack(pady=20)

# Función para generar el reporte de asistencia
def generate_attendance_report(selected_date):
    # Verificar si la fecha ingresada no está vacía
    if not selected_date:
        messagebox.showerror("Error", "Por favor ingrese una fecha válida en el formato YYYY-MM-DD.")
        return

    # Verificar si la fecha está en formato correcto (YYYY-MM-DD)
    try:
        datetime.datetime.strptime(selected_date, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Error", "La fecha ingresada no tiene el formato correcto. Use YYYY-MM-DD.")
        return

    # Llamar al controlador para obtener los datos del reporte de asistencia para la fecha seleccionada
    success, data = generate_attendance_report_by_date(selected_date)
    
    # Verificar si se obtuvieron los datos correctamente
    if not success:
        messagebox.showerror("Error", f"No se pudo obtener el reporte de asistencias para la fecha: {selected_date}.")
        return

    # Verificar si hay datos disponibles
    if len(data) == 0:
        messagebox.showerror("Error", f"No hay datos de asistencia para la fecha: {selected_date}.")
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
