from tkinter import Toplevel, Label, Button, StringVar, OptionMenu, Entry
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter import messagebox 
from datetime import datetime

def generate_certificate(certificate_type, first_name, last_name, id_number, year):
    file_name = f"Certificate_{certificate_type}_{first_name}_{last_name}.pdf"
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter

    logo1_path = "assets/login/records1.jpeg"
    logo2_path = "assets/login/records2.jpeg"

    logo_y_position = height - 150  
    logo_width = 120
    logo_height = 120

    c.drawImage(logo1_path, 40, logo_y_position, width=logo_width, height=logo_height)  
    c.drawImage(logo2_path, width - 160, logo_y_position, width=logo_width, height=logo_height)  

    HEADER = """
    Republica Bolivariana de Venezuela
    Ministerio del Poder Popular Para la Educación Media
    Liceo Nacional Jose Felix Ribas
    """
    c.setFont("Helvetica", 12)
    
    header_lines = HEADER.strip().splitlines()
    header_start_y = logo_y_position + 40  
    line_height = 14

    for i, line in enumerate(header_lines):
        text_width = c.stringWidth(line, "Helvetica", 12)
        c.drawString((width - text_width) / 2, header_start_y - i * line_height, line)

    # Translate the title based on the certificate type
    if certificate_type == "Estudio":
        title = "Constancia de Estudio"
    elif certificate_type == "Buen Comportamiento":
        title = "Constancia de Buen Comportamiento"
    else:
        title = "Constancia"

    c.setFont("Helvetica-Bold", 16)
    text_width = c.stringWidth(title, "Helvetica-Bold", 16)
    c.drawString((width - text_width) / 2, header_start_y - (len(header_lines) * line_height) - 60, title)

    c.setFont("Helvetica", 12)

    current_date = datetime.now().strftime("%d/%m/%Y")

    full_name = f"{first_name} {last_name}"

    if certificate_type == "Estudio":
        text = f"""
        Quien suscribe: LCDO Asdrubal Zambrano, DIRECTOR(A) del
        Liceo Nacional Jose Felix Ribas Ubicado en el Chicaro Estado Tachira,
        hace constar que: {full_name}, con cédula de ciudadanía número {id_number},
        quien cursa el año: {year}, ha sido alumno/a regular en nuestra institución.
        """
    elif certificate_type == "Buen Comportamiento":
        text = f"""
        Se hace constar que el estudiante {full_name}, con cédula de ciudadanía 
        número {id_number}, ha cursado sus estudios en el Liceo Nacional Jose Felix Ribas
        desde {current_date} hasta la fecha. Durante todo este tiempo, el estudiante ha
        demostrado un comportamiento ejemplar, caracterizado por su respeto hacia los
        profesores y compañeros, su puntualidad y su compromiso con las actividades académicas.

        Por lo tanto, se le extiende la presente constancia como reconocimiento
        a su buen desempeño y conducta.
        """
    else:
        text = f"Este es un certificado genérico para {full_name}."

    lines = text.splitlines()
    text_start_y = header_start_y - (len(header_lines) * line_height) - 150 
    
    for i, line in enumerate(lines):
        line = line.strip()
        text_width = c.stringWidth(line, "Helvetica", 12)
        
        c.drawString((width - text_width) / 2, text_start_y - i * line_height, line)

    spacing = 227  
    
    issue_date = f"Expedido el {current_date}"  
    date_text_width = c.stringWidth(issue_date, "Helvetica", 12)
    c.drawString((width - date_text_width) / 2, text_start_y - (len(lines) * line_height) - spacing, issue_date)

    signature_text = """
    _____________________________
    Firma del Director(a)
    """
    signature_lines = signature_text.strip().splitlines()
    
    signature_start_y = text_start_y - (len(lines) * line_height) - spacing - 10  

    for i, line in enumerate(signature_lines):
        text_width = c.stringWidth(line, "Helvetica", 12)
        c.drawString((width - text_width) / 2, signature_start_y - i * line_height, line)

    c.showPage()
    c.save()

    messagebox.showinfo("Generación Exitosa", f"El certificado de {certificate_type} ha sido generado con éxito.")