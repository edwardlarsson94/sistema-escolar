from tkinter import Toplevel, Label, Button, StringVar, OptionMenu, Entry
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_certificate(certificate_type, first_name, last_name, id_number, year, behavior):
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
    if certificate_type == "Study":
        title = "Constancia de Estudio"
    elif certificate_type == "Good Behavior":
        title = "Constancia de Buen Comportamiento"

    c.setFont("Helvetica-Bold", 16)
    text_width = c.stringWidth(title, "Helvetica-Bold", 16)
    c.drawString((width - text_width) / 2, header_start_y - (len(header_lines) * line_height) - 60, title)

    c.setFont("Helvetica", 12)

    current_date = datetime.now().strftime("%d/%m/%Y")

    full_name = f"{first_name} {last_name}"

    if certificate_type == "Study":
        text = f"""
        Quien suscribe: LDA YARITH MARCELA CÁRDENAS GALVIS,
        DIRECTOR(A) de la DIRECCIÓN DE REGISTRO Y CONTROL DE ACTIVIDADES ACADÉMICAS,
        en la UNIVERSIDAD POLITÉCNICA TERRITORIAL AGROANDINA DEL ESTADO TÁCHIRA,
        hace constar que: {full_name}, con cédula de ciudadanía número {id_number},
        quien cursa el año: {year}, ha sido alumno/a regular en nuestra institución.
        """
    elif certificate_type == "Good Behavior":
        text = f"""
        Se hace constar que la estudiante {full_name}, con cédula de ciudadanía 
        número {id_number}, ha cursado sus estudios en el Liceo Nacional Jose Felix Ribas
        desde {current_date} hasta la fecha. Durante todo este tiempo, el estudiante ha
        demostrado un comportamiento ejemplar, caracterizado por su respeto hacia los
        profesores y compañeros, su puntualidad y su compromiso con las actividades académicas.

        Por lo tanto, se le extiende la presente constancia como reconocimiento
        a su buen desempeño y conducta.
        """

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

    print(f"Certificate of {certificate_type} generated successfully: {file_name}")

def create_form():
    def generate():
        first_name = first_name_var.get()
        last_name = last_name_var.get()
        id_number = id_number_var.get()
        year = year_var.get()
        certificate_type = type_var.get()
        behavior = behavior_var.get() if certificate_type == "Good Behavior" else None
        generate_certificate(certificate_type, first_name, last_name, id_number, year, behavior)

    form_window = Toplevel()
    form_window.title("Generar Constancia")
    
    first_name_var = StringVar()
    last_name_var = StringVar()
    id_number_var = StringVar()
    year_var = StringVar()
    type_var = StringVar(value="Estudio")
    behavior_var = StringVar(value="Excelente")
    
    form_window.configure(bg="#1A237E")

    Label(form_window, text="Nombres:", bg="#1A237E", fg='white').grid(row=0, column=0)
    Entry(form_window, textvariable=first_name_var).grid(row=0, column=1)
    
    Label(form_window, text="Apellidos:", bg="#1A237E", fg='white').grid(row=1, column=0)
    Entry(form_window, textvariable=last_name_var).grid(row=1, column=1)

    Label(form_window, text="Cédula:", bg="#1A237E", fg='white').grid(row=2, column=0)
    Entry(form_window, textvariable=id_number_var).grid(row=2, column=1)
    
    Label(form_window, text="Año/Clase:", bg="#1A237E", fg='white').grid(row=3, column=0)
    Entry(form_window, textvariable=year_var).grid(row=3, column=1)
    
    Label(form_window, text="Tipo de Constancia:", bg="#1A237E", fg='white').grid(row=4, column=0)
    OptionMenu(form_window, type_var, "Estudio", "Buen Comportamiento").grid(row=4, column=1)
    
    Label(form_window, text="Comportamiento (si aplica):", bg="#1A237E", fg='white').grid(row=5, column=0)
    Entry(form_window, textvariable=behavior_var).grid(row=5, column=1)

    Button(form_window, text="Generar Constancia", command=generate, bg='red', fg='white').grid(row=6, column=0, columnspan=2)

