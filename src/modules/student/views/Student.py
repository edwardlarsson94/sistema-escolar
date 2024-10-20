import tkinter as tk
from tkinter import ttk
import re
from datetime import datetime
from tkinter import messagebox 
from api.controllers.studentController import add_student_with_relations, delete_student, fetch_student_details, update_student_with_relations
from components.Table import populate_table
from constants.Colors import (BACKGROUND_COLOR, TITLE_COLOR, BUTTON_COLOR, BUTTON_TEXT_COLOR, BUTTON_COLOR_HOVER, ENTRY_BACKGROUND, ENTRY_FOREGROUND)
from constants.Texts import (STUDENT_TITLE_EDIT, GLOBAL_STUDENT_TITLE_ADD, GLOBAL_CONFIRM_DELETE, GLOBAL_TABLE_NIT, GLOBAL_TABLE_NAME, GLOBAL_BUTTON_SAVE, GLOBAL_BUTTON_CONFIRM, GLOBAL_BUTTON_CANCEL, GLOBAL_LAST_NAME, GLOBAL_AGE, GLOBAL_SEX, GLOBAL_ADDRESS, GLOBAL_COURSE, GLOBAL_PHONE)
from src.modules.records.Records import generate_certificate
from tkinter import Toplevel, Label, StringVar, OptionMenu, Entry, Button, messagebox

fields = [
    ("Cédula", GLOBAL_TABLE_NIT),
    ("Nombres", GLOBAL_TABLE_NAME),
    ("Apellidos", GLOBAL_LAST_NAME),
    ("Lugar de Nacimiento", 'Lugar de Nacimiento'),
    ("Nacionalidad", 'Nacionalidad'),
    ("Edad", GLOBAL_AGE),
    ("Día de Nacimiento", "Día de Nacimiento"),
    ("Mes de Nacimiento", "Mes de Nacimiento"),
    ("Año de Nacimiento", "Año de Nacimiento"),
    ("Plantel de Procedencia", 'Plantel de Procedencia'),
    ("Trae Materia Pendiente", 'Trae Materia Pendiente'),
    ("¿Cuál?", '¿Cuál?'),
    ("Dirección", GLOBAL_ADDRESS),
    ("Repite", 'Repite'),
    ("¿Con Cuáles?", '¿Con Cuáles?'),
    ("¿Vive con sus Padres?", '¿Vive con sus Padres?'),
    ("Correo Electrónico", 'Correo Electrónico'),
    ("Religión", 'Religión'),
    ("Sexo", GLOBAL_SEX),
    ("Año que cursa", GLOBAL_COURSE),
    ("Teléfono", GLOBAL_PHONE)
]

family_fields = [
    ("Nombre del Padre", "Nombre del Padre"),
    ("Nombre de la Madre", "Nombre de la Madre"),
    ("Cédula del Padre", "Cédula del Padre"),
    ("Cédula de la Madre", "Cédula de la Madre"),
    ("Teléfono del Padre", "Teléfono del Padre"),
    ("Teléfono de la Madre", "Teléfono de la Madre"),
    ("Oficio del Padre", "Oficio del Padre"),
    ("Oficio de la Madre", "Oficio de la Madre"),
    ("Correo del Padre", "Correo del Padre"),
    ("Correo de la Madre", "Correo de la Madre")
]

representative_fields = [
    ("Nombre Representante", "Nombre Representante"),
    ("Cédula Representante", "Cédula Representante"),
    ("Oficio Representante", "Oficio Representante"),
    ("Parentesco al Alumno", "Parentesco al Alumno"),
    ("Direccion Domicilio", "Direccion Domicilio"),
    ("Teléfono Habitación", "Teléfono Habitación"),
    ("Teléfono Trabajo", "Teléfono Trabajo"),
    ("Teléfono Celular", "Teléfono Celular"),
    ("Correo Electrónico", "Correo Electrónico"),
    ("Autoriza en ausencia", "Autoriza en ausencia"),
    ("Cedula del autorizado", "Cedula del autorizado"),
]

# Actions

def get_entry_value(entry):
    return entry.get() if entry.get() else ""


def add_student(tree, *args):
    # Extraer los datos de los argumentos
    student_data = args[:21]  # Primeros 21 argumentos son datos del estudiante
    family_data = args[21:31]  # Siguientes 10 argumentos son datos familiares
    representative_data = args[31:42]  # Últimos 11 argumentos son datos del representante
    new_window = args[-1]  # El último argumento es la ventana

    # Validar todos los datos antes de proceder
    if not all([
        validate_student_data(student_data),
        validate_family_data(family_data),
        validate_representative_data(representative_data)
    ]):
        return

    # Si todas las validaciones pasan, proceder con el guardado
    success, message = add_student_with_relations(student_data, family_data, representative_data)
    
    if success:
        messagebox.showinfo("Registro Exitoso", message)
        tree.insert("", "end", values=student_data)
        populate_table(tree)
        new_window.destroy()
    else:
        messagebox.showerror("Error", message)

def update_student(tree, selected_item, student_id, *args):
    # Extraer los datos de los argumentos
    student_data = args[:21]  # Primeros 21 argumentos son datos del estudiante
    family_data = args[21:31]  # Siguientes 10 argumentos son datos familiares
    representative_data = args[31:42]  # Últimos 11 argumentos son datos del representante
    new_window = args[-1]  # El último argumento es la ventana

    # Validar todos los datos antes de proceder
    if not all([
        validate_student_data(student_data),
        validate_family_data(family_data),
        validate_representative_data(representative_data)
    ]):
        return

    # Si todas las validaciones pasan, proceder con la actualización
    success, message = update_student_with_relations(student_id, student_data, family_data, representative_data)
    
    if success:
        messagebox.showinfo("Actualización Exitosa", message)
        tree.item(selected_item, values=(student_data + family_data + representative_data))
        populate_table(tree)
        new_window.destroy()
    else:
        messagebox.showerror("Error", message)
        
        
def confirm_delete_student(tree, selected_item, student_id):
    new_window = tk.Toplevel()
    new_window.title(GLOBAL_CONFIRM_DELETE)
    new_window.geometry("300x150")
    new_window.configure(bg=BACKGROUND_COLOR)

    label_message = tk.Label(new_window, text=f"¿Estás seguro de que deseas borrar al estudiante con cédula {student_id}?", 
                             bg=BACKGROUND_COLOR, fg=TITLE_COLOR, wraplength=250)
    label_message.pack(pady=10)

    def delete_confirmed():
        success, message = delete_student(student_id)
        
        if success:
            tree.delete(selected_item)
            messagebox.showinfo("Borrado Exitoso", message)
        else:
            messagebox.showerror("Error", message)
        
        new_window.destroy()

    button_confirm = tk.Button(new_window, text=GLOBAL_BUTTON_CONFIRM, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, 
                               command=delete_confirmed)
    button_cancel = tk.Button(new_window, text=GLOBAL_BUTTON_CANCEL, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, 
                              command=new_window.destroy)

    button_confirm.bind("<Enter>", on_enter)
    button_confirm.bind("<Leave>", on_leave)
    button_cancel.bind("<Enter>", on_enter)
    button_cancel.bind("<Leave>", on_leave)

    button_confirm.pack(side="left", padx=20, pady=20)
    button_cancel.pack(side="right", padx=20, pady=20)

def generate_pdf_for_student(student_id):
    student_data, _, _ = fetch_student_details(student_id)
    if student_data is None:
        messagebox.showerror("Error", "No se encontraron datos para el estudiante seleccionado.")
        return

    first_name = student_data[2] if len(student_data) > 2 else "Nombre desconocido"
    last_name = student_data[3] if len(student_data) > 3 else "Apellido desconocido"
    id_number = student_data[1] if len(student_data) > 1 else "ID desconocido"
    year = student_data[20] if len(student_data) > 20 else "Año desconocido"
    
    generate_certificate_form(first_name, last_name, id_number, year)
# Opens Windows

def open_new_student_form(tree):
    new_window = tk.Toplevel()
    new_window.title(GLOBAL_STUDENT_TITLE_ADD)
    new_window.geometry("1200x450")
    new_window.configure(bg=BACKGROUND_COLOR)

    # Crear un Notebook (pestañas)
    notebook = ttk.Notebook(new_window)
    notebook.pack(expand=True, fill='both', padx=20, pady=20)

    # Pestaña de datos del estudiante
    student_frame = tk.Frame(notebook, bg=BACKGROUND_COLOR)
    notebook.add(student_frame, text="Datos del Estudiante")

    # Pestaña de datos del familiar
    family_frame = tk.Frame(notebook, bg=BACKGROUND_COLOR)
    notebook.add(family_frame, text="Datos del Familiar")

    # Pestaña de datos del representante
    representative_frame = tk.Frame(notebook, bg=BACKGROUND_COLOR)
    notebook.add(representative_frame, text="Datos del Representante")

    # Definir campos para la pestaña de Datos del Estudiante

    entries = {}

    # Crear los campos en la pestaña de Datos del Estudiante
    for i, (field, label_text) in enumerate(fields):
        row = i // 3  # Cada tres campos en una nueva fila
        col = i % 3   # Distribuir en 3 columnas

        label = tk.Label(student_frame, text=label_text, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
        label.grid(row=row, column=col * 2, padx=(10, 5), pady=5, sticky='e')

        entry = tk.Entry(student_frame, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
        entry.grid(row=row, column=(col * 2) + 1, padx=(0, 10), pady=5, sticky='w')
        entries[field] = entry

    for i, (field, label_text) in enumerate(family_fields):
        row = i // 3  # Cada tres campos en una nueva fila
        col = i % 3   # Distribuir en 3 columnas
    
        label = tk.Label(family_frame, text=label_text, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
        label.grid(row=row, column=col * 2, padx=(10, 5), pady=5, sticky='e')

        entry = tk.Entry(family_frame, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
        entry.grid(row=row, column=(col * 2) + 1, padx=(0, 10), pady=5, sticky='w')
        entries[field] = entry


    for i, (field, label_text) in enumerate(representative_fields):
        row = i // 3  # Cada tres campos en una nueva fila
        col = i % 3   # Distribuir en 3 columnas

        label = tk.Label(representative_frame, text=label_text, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
        label.grid(row=row, column=col * 2, padx=(10, 5), pady=5, sticky='e')

        entry = tk.Entry(representative_frame, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
        entry.grid(row=row, column=(col * 2) + 1, padx=(0, 10), pady=5, sticky='w')
        entries[field] = entry

    # Botón de guardar
    save_button = tk.Button(new_window, text=GLOBAL_BUTTON_SAVE, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                            command=lambda: add_student(tree, 
                                                        
                                                        get_entry_value(entries["Cédula"]),
                                                        get_entry_value(entries["Nombres"]),
                                                        get_entry_value(entries["Apellidos"]),
                                                        get_entry_value(entries["Lugar de Nacimiento"]),
                                                        get_entry_value(entries["Nacionalidad"]),
                                                        get_entry_value(entries["Edad"]),
                                                        get_entry_value(entries["Día de Nacimiento"]),
                                                        get_entry_value(entries["Mes de Nacimiento"]),
                                                        get_entry_value(entries["Año de Nacimiento"]),
                                                        get_entry_value(entries["Plantel de Procedencia"]),
                                                        get_entry_value(entries["Trae Materia Pendiente"]),
                                                        get_entry_value(entries["¿Cuál?"]),
                                                        get_entry_value(entries["Dirección"]),
                                                        get_entry_value(entries["Repite"]),
                                                        get_entry_value(entries["¿Con Cuáles?"]),
                                                        get_entry_value(entries["¿Vive con sus Padres?"]),
                                                        get_entry_value(entries["Correo Electrónico"]),
                                                        get_entry_value(entries["Religión"]),
                                                        get_entry_value(entries["Sexo"]),
                                                        get_entry_value(entries["Año que cursa"]),
                                                        get_entry_value(entries["Teléfono"]),

                                                        get_entry_value(entries["Nombre del Padre"]),
                                                        get_entry_value(entries["Nombre de la Madre"]),
                                                        get_entry_value(entries["Cédula del Padre"]),
                                                        get_entry_value(entries["Cédula de la Madre"]),
                                                        get_entry_value(entries["Teléfono del Padre"]),
                                                        get_entry_value(entries["Teléfono de la Madre"]),
                                                        get_entry_value(entries["Oficio del Padre"]),
                                                        get_entry_value(entries["Oficio de la Madre"]),
                                                        get_entry_value(entries["Correo del Padre"]),
                                                        get_entry_value(entries["Correo de la Madre"]),

                                                        get_entry_value(entries["Nombre Representante"]),
                                                        get_entry_value(entries["Cédula Representante"]),                                                        
                                                        get_entry_value(entries["Oficio Representante"]),
                                                        get_entry_value(entries["Parentesco al Alumno"]),
                                                        get_entry_value(entries["Direccion Domicilio"]),
                                                        get_entry_value(entries["Teléfono Habitación"]),
                                                        get_entry_value(entries["Teléfono Trabajo"]),
                                                        get_entry_value(entries["Teléfono Celular"]),
                                                        get_entry_value(entries["Correo Electrónico"]),
                                                        get_entry_value(entries["Autoriza en ausencia"]),
                                                        get_entry_value(entries["Cedula del autorizado"]),

                                                        new_window))
    save_button.pack(pady=20)
    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)

def open_edit_student_form(tree, selected_item, student_id):    
    student_data, family_data, representative_data = fetch_student_details(student_id)
    
    if student_data is None or family_data is None or representative_data is None:
        messagebox.showerror("Error", "No se encontraron datos para el estudiante seleccionado.")
        return
    
    new_window = tk.Toplevel()
    new_window.title(STUDENT_TITLE_EDIT)
    new_window.geometry("1200x500")
    new_window.configure(bg=BACKGROUND_COLOR)

    notebook = ttk.Notebook(new_window)
    notebook.pack(expand=True, fill='both', padx=20, pady=20)

    student_frame = tk.Frame(notebook, bg=BACKGROUND_COLOR)
    notebook.add(student_frame, text="Datos del Estudiante")

    family_frame = tk.Frame(notebook, bg=BACKGROUND_COLOR)
    notebook.add(family_frame, text="Datos del Familiar")

    representative_frame = tk.Frame(notebook, bg=BACKGROUND_COLOR)
    notebook.add(representative_frame, text="Datos del Representante")

    entries = {}

    for i, (field, label_text) in enumerate(fields):
        row = i // 3
        col = i % 3

        label = tk.Label(student_frame, text=label_text, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
        label.grid(row=row, column=col * 2, padx=(10, 5), pady=5, sticky='e')

        entry = tk.Entry(student_frame, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
        entry.insert(0, student_data[i + 1] if student_data and len(student_data) > i else "")
        entry.grid(row=row, column=(col * 2) + 1, padx=(0, 10), pady=5, sticky='w')
        entries[field] = entry

    for i, (field, label_text) in enumerate(family_fields):
        row = i // 3
        col = i % 3
    
        label = tk.Label(family_frame, text=label_text, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
        label.grid(row=row, column=col * 2, padx=(10, 5), pady=5, sticky='e')

        entry = tk.Entry(family_frame, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
        entry.insert(0, family_data[i + 1] if family_data and len(family_data) > i else "")
        entry.grid(row=row, column=(col * 2) + 1, padx=(0, 10), pady=5, sticky='w')
        entries[field] = entry

    for i, (field, label_text) in enumerate(representative_fields):
        row = i // 3
        col = i % 3
    
        label = tk.Label(representative_frame, text=label_text, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
        label.grid(row=row, column=col * 2, padx=(10, 5), pady=5, sticky='e')

        entry = tk.Entry(representative_frame, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
        entry.insert(0, representative_data[i + 1] if representative_data and len(representative_data) > i else "")
        entry.grid(row=row, column=(col * 2) + 1, padx=(0, 10), pady=5, sticky='w')
        entries[field] = entry

    save_button = tk.Button(new_window, text=GLOBAL_BUTTON_SAVE, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                            command=lambda: update_student(
                                tree, selected_item, student_id,
                                entries["Cédula"].get(),
                                entries["Nombres"].get(),
                                entries["Apellidos"].get(),
                                entries["Lugar de Nacimiento"].get(),
                                entries["Nacionalidad"].get(),
                                entries["Edad"].get(),
                                entries["Día de Nacimiento"].get(),
                                entries["Mes de Nacimiento"].get(),
                                entries["Año de Nacimiento"].get(),
                                entries["Plantel de Procedencia"].get(),
                                entries["Trae Materia Pendiente"].get(),
                                entries["¿Cuál?"].get(),
                                entries["Dirección"].get(),
                                entries["Repite"].get(),
                                entries["¿Con Cuáles?"].get(),
                                entries["¿Vive con sus Padres?"].get(),
                                entries["Correo Electrónico"].get(),
                                entries["Religión"].get(),
                                entries["Sexo"].get(),
                                entries["Año que cursa"].get(),
                                entries["Teléfono"].get(),

                                entries["Nombre del Padre"].get(),
                                entries["Nombre de la Madre"].get(),
                                entries["Cédula del Padre"].get(),
                                entries["Cédula de la Madre"].get(),
                                entries["Teléfono del Padre"].get(),
                                entries["Teléfono de la Madre"].get(),
                                entries["Oficio del Padre"].get(),
                                entries["Oficio de la Madre"].get(),
                                entries["Correo del Padre"].get(),                                
                                entries["Correo de la Madre"].get(),
                                
                                entries["Nombre Representante"].get(),                                
                                entries["Cédula Representante"].get(),                                
                                entries["Oficio Representante"].get(),
                                entries["Parentesco al Alumno"].get(),
                                entries["Direccion Domicilio"].get(),
                                entries["Teléfono Habitación"].get(),
                                entries["Teléfono Trabajo"].get(),
                                entries["Teléfono Celular"].get(),
                                entries["Correo Electrónico"].get(),
                                entries["Autoriza en ausencia"].get(),
                                entries["Cedula del autorizado"].get(),

                                new_window))

    save_button.pack(pady=20)
    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)

def open_student_details(student_id):
    if isinstance(student_id, tuple) and len(student_id) > 0:
        student_id_str = student_id[0]
        student_id = int(''.join(filter(str.isdigit, student_id_str)))

    student_data, family_data, representative_data = fetch_student_details(student_id)

    if student_data is None and family_data is None and representative_data is None:
        messagebox.showerror("Error", "No se encontraron datos para el estudiante con el ID proporcionado.")
        return
    details_window = tk.Toplevel()
    details_window.title("Detalles del Estudiante")
    details_window.geometry("800x500")
    details_window.configure(bg=BACKGROUND_COLOR)

    notebook = ttk.Notebook(details_window)
    notebook.pack(expand=True, fill='both', padx=20, pady=20)

    # Pestaña de datos del estudiante
    student_frame = tk.Frame(notebook, bg=BACKGROUND_COLOR)
    notebook.add(student_frame, text="Datos del Estudiante")

    # Pestaña de datos del familiar
    family_frame = tk.Frame(notebook, bg=BACKGROUND_COLOR)
    notebook.add(family_frame, text="Datos del Familiar")

    # Pestaña de datos del representante
    representative_frame = tk.Frame(notebook, bg=BACKGROUND_COLOR)
    notebook.add(representative_frame, text="Datos del Representante")

    # Llenar datos del estudiante
    for i, (field, label_text) in enumerate(fields):
        row = i // 3
        col = i % 3

        label = tk.Label(student_frame, text=f"{label_text}:", bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=("Helvetica", 12))
        label.grid(row=row, column=col * 2, padx=(10, 5), pady=5, sticky='e')

        value = student_data[i + 1] if student_data and len(student_data) > i else "N/A"
        value_label = tk.Label(student_frame, text=value, bg=BACKGROUND_COLOR, fg=ENTRY_FOREGROUND, font=("Helvetica", 12))
        value_label.grid(row=row, column=(col * 2) + 1, padx=(0, 10), pady=5, sticky='w')

    # Mostrar campos en la pestaña de Datos del Familiar
    for i, (field, label_text) in enumerate(family_fields):
        row = i // 3
        col = i % 3

        label = tk.Label(family_frame, text=f"{label_text}:", bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=("Helvetica", 12))
        label.grid(row=row, column=col * 2, padx=(10, 5), pady=5, sticky='e')

        value = family_data[i + 1] if family_data and len(family_data) > i else "N/A"
        value_label = tk.Label(family_frame, text=value, bg=BACKGROUND_COLOR, fg=ENTRY_FOREGROUND, font=("Helvetica", 12))
        value_label.grid(row=row, column=(col * 2) + 1, padx=(0, 10), pady=5, sticky='w')

    # Mostrar campos en la pestaña de Datos del Representante
    for i, (field, label_text) in enumerate(representative_fields):
        row = i // 3
        col = i % 3
    
        label = tk.Label(representative_frame, text=f"{label_text}:", bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=("Helvetica", 12))
        label.grid(row=row, column=col * 2, padx=(10, 5), pady=5, sticky='e')

        value = representative_data[i + 1] if representative_data and len(representative_data) > i else "N/A"
        value_label = tk.Label(representative_frame, text=value, bg=BACKGROUND_COLOR, fg=ENTRY_FOREGROUND, font=("Helvetica", 12))
        value_label.grid(row=row, column=(col * 2) + 1, padx=(0, 10), pady=5, sticky='w')

    close_button = tk.Button(details_window, text="Cerrar", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, command=details_window.destroy)
    close_button.pack(pady=10)
    close_button.bind("<Enter>", on_enter)
    close_button.bind("<Leave>", on_leave)

def generate_certificate_form(first_name, last_name, id_number, year):

    form_window = Toplevel()
    form_window.title("Generar Certificado")
    form_window.configure(bg="#1A237E")
    
    first_name_var = StringVar(value=first_name)
    last_name_var = StringVar(value=last_name)
    id_number_var = StringVar(value=id_number)
    year_var = StringVar(value=year)
    type_var = StringVar(value="Estudio")  # Tipo de certificado
    behavior_var = StringVar(value="Excelente")  # Comportamiento para el certificado de buen comportamiento

    # Campos de entrada
    Label(form_window, text="Nombres:", bg="#1A237E", fg='white').grid(row=0, column=0, sticky='e', padx=5, pady=5)
    Entry(form_window, textvariable=first_name_var).grid(row=0, column=1, padx=5, pady=5)
    
    Label(form_window, text="Apellidos:", bg="#1A237E", fg='white').grid(row=1, column=0, sticky='e', padx=5, pady=5)
    Entry(form_window, textvariable=last_name_var).grid(row=1, column=1, padx=5, pady=5)

    Label(form_window, text="Cédula:", bg="#1A237E", fg='white').grid(row=2, column=0, sticky='e', padx=5, pady=5)
    Entry(form_window, textvariable=id_number_var).grid(row=2, column=1, padx=5, pady=5)
    
    Label(form_window, text="Año/Clase:", bg="#1A237E", fg='white').grid(row=3, column=0, sticky='e', padx=5, pady=5)
    Entry(form_window, textvariable=year_var).grid(row=3, column=1, padx=5, pady=5)
    
    Label(form_window, text="Tipo de Certificado:", bg="#1A237E", fg='white').grid(row=4, column=0, sticky='e', padx=5, pady=5)
    OptionMenu(form_window, type_var, "Estudio", "Buena Conducta").grid(row=4, column=1, padx=5, pady=5)
    
    # Botón de generación de certificado
    Button(form_window, text="Generar Certificado", command=lambda: confirm_generate_certificate(form_window, type_var.get(), first_name_var.get(), last_name_var.get(), id_number_var.get(), year_var.get()), bg='green', fg='white').grid(row=6, column=0, columnspan=2, pady=10)

# Handlesp

class FieldValidation:
    @staticmethod
    def validate_required_field(value, field_name):
        """Validates that a required field is not empty"""
        if not value or value.strip() == "":
            raise ValueError(f"El campo {field_name} es requerido")
        return value.strip()

    @staticmethod
    def validate_nit(value):
        """Validates Venezuelan ID format (V-xxxxxxxx or E-xxxxxxxx)"""
        if not value:
            raise ValueError("La cédula es requerida")
        
        pattern = r'^[VE]-\d{7,8}$'
        if not re.match(pattern, value):
            raise ValueError("Formato de cédula inválido. Debe ser V-xxxxxxxx o E-xxxxxxxx")
        return value

    @staticmethod
    def validate_name(value, field_name):
        """Validates that a name contains only letters, spaces, and common special characters"""
        if not value:
            raise ValueError(f"El {field_name} es requerido")
        
        pattern = r'^[A-Za-zÁáÉéÍíÓóÚúÑñ\s\'-]+$'
        if not re.match(pattern, value):
            raise ValueError(f"El {field_name} solo debe contener letras y espacios")
        return value.strip()

    @staticmethod
    def validate_age(value):
        """Validates that age is a number between 1 and 100"""
        if not value:
            raise ValueError("La edad es requerida")
        
        try:
            age = int(value)
            if not 1 <= age <= 100:
                raise ValueError("La edad debe estar entre 1 y 100 años")
        except ValueError:
            raise ValueError("La edad debe ser un número válido")
        return value

    @staticmethod
    def validate_date(day, month, year):
        """Validates that a date is valid and not in the future"""
        if not all([day, month, year]):
            raise ValueError("La fecha de nacimiento completa es requerida")
        
        try:
            day = int(day)
            month = int(month)
            year = int(year)
            birth_date = datetime(year, month, day)
            
            if birth_date > datetime.now():
                raise ValueError("La fecha de nacimiento no puede ser futura")
            
            return True
        except ValueError as e:
            raise ValueError("Fecha de nacimiento inválida")

    @staticmethod
    def validate_email(value, field_name="Correo electrónico"):
        """Validates email format"""
        if not value:  # Si el email es opcional
            return value
        
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, value):
            raise ValueError(f"{field_name} inválido")
        return value

    @staticmethod
    def validate_phone(value, field_name="Teléfono"):
        """Validates phone number format"""
        if not value:  # Si el teléfono es opcional
            return value
        
        pattern = r'^\+?\d{10,15}$'
        if not re.match(pattern, value):
            raise ValueError(f"{field_name} inválido. Debe contener entre 10 y 15 dígitos")
        return value

    @staticmethod
    def validate_course(value):
        """Validates that course is a valid year"""
        valid_courses = ["1er", "2do", "3er", "4to", "5to"]
        if value not in valid_courses:
            raise ValueError("Año de curso inválido")
        return value

    @staticmethod
    def validate_sex(value):
        """Validates sex field"""
        valid_options = ["M", "F"]
        if value.upper() not in valid_options:
            raise ValueError("Sexo debe ser M o F")
        return value.upper()

    @staticmethod
    def validate_boolean_field(value, field_name):
        """Validates fields that should be Si or No"""
        valid_options = ["Si", "No"]
        if value and value not in valid_options:
            raise ValueError(f"El campo {field_name} debe ser Si o No")
        return value

def validate_student_data(student_data):
    """Validates all student fields before saving/updating"""
    validator = FieldValidation()
    
    # Desempaquetar los datos del estudiante
    (nit, name, lastName, birth_place, nationality, age, birth_day,
     birth_month, birth_year, previous_school, pending_subject, which_subject,
     address, repeating, which_subjects, lives_with_parents, email, religion,
     sex, course, phone) = student_data

    try:
        # Validaciones principales
        validator.validate_nit(nit)
        validator.validate_name(name, "nombre")
        validator.validate_name(lastName, "apellido")
        validator.validate_required_field(birth_place, "lugar de nacimiento")
        validator.validate_required_field(nationality, "nacionalidad")
        validator.validate_age(age)
        validator.validate_date(birth_day, birth_month, birth_year)
        validator.validate_required_field(previous_school, "plantel de procedencia")
        validator.validate_boolean_field(pending_subject, "materia pendiente")
        validator.validate_required_field(address, "dirección")
        validator.validate_boolean_field(repeating, "repite")
        validator.validate_boolean_field(lives_with_parents, "vive con sus padres")
        validator.validate_email(email)
        validator.validate_required_field(religion, "religión")
        validator.validate_sex(sex)
        validator.validate_course(course)
        validator.validate_phone(phone)

        return True

    except ValueError as e:
        messagebox.showerror("Error de Validación", str(e))
        return False

def validate_family_data(family_data):
    """Validates all family fields before saving/updating"""
    validator = FieldValidation()
    
    (name_of_parent, name_of_mother, nit_of_parent, nit_of_mother,
     phone_of_parent, phone_of_mother, office_of_parent, office_of_mother,
     email_of_parent, email_of_mother) = family_data

    try:
        # Validar al menos un padre/madre
        if not (name_of_parent or name_of_mother):
            raise ValueError("Debe proporcionar información de al menos un padre o madre")

        # Validaciones condicionales para el padre
        if name_of_parent:
            validator.validate_name(name_of_parent, "nombre del padre")
            validator.validate_nit(nit_of_parent)
            validator.validate_phone(phone_of_parent, "teléfono del padre")
            validator.validate_required_field(office_of_parent, "oficio del padre")
            validator.validate_email(email_of_parent, "correo del padre")

        # Validaciones condicionales para la madre
        if name_of_mother:
            validator.validate_name(name_of_mother, "nombre de la madre")
            validator.validate_nit(nit_of_mother)
            validator.validate_phone(phone_of_mother, "teléfono de la madre")
            validator.validate_required_field(office_of_mother, "oficio de la madre")
            validator.validate_email(email_of_mother, "correo de la madre")

        return True

    except ValueError as e:
        messagebox.showerror("Error de Validación", str(e))
        return False

def validate_representative_data(representative_data):
    """Validates all representative fields before saving/updating"""
    validator = FieldValidation()
    
    (name_of_representative, nit_of_representative, office_of_representative,
     relationship_to_student, address_of_house, phone_of_house, phone_of_work,
     phone_of_cellular, email_of_representative, authorized_in_absence,
     authorized_person_id) = representative_data

    try:
        # Validaciones del representante
        validator.validate_name(name_of_representative, "nombre del representante")
        validator.validate_nit(nit_of_representative)
        validator.validate_required_field(office_of_representative, "oficio del representante")
        validator.validate_required_field(relationship_to_student, "parentesco")
        validator.validate_required_field(address_of_house, "dirección")
        validator.validate_phone(phone_of_house, "teléfono de habitación")
        validator.validate_phone(phone_of_work, "teléfono de trabajo")
        validator.validate_phone(phone_of_cellular, "teléfono celular")
        validator.validate_email(email_of_representative, "correo del representante")
        
        # Validaciones para persona autorizada
        if authorized_in_absence == "Si":
            validator.validate_nit(authorized_person_id)

        return True

    except ValueError as e:
        messagebox.showerror("Error de Validación", str(e))
        return False

def on_click_action(tree, edit_button, delete_button, details_button, pdf_button, reports_button):
    selected_item = tree.selection()
    if selected_item:
        selected_student = tree.item(selected_item, 'values')
        student_id = selected_student[0]
        edit_button.config(state="normal", command=lambda: open_edit_student_form(tree, selected_item, student_id))
        delete_button.config(state="normal", command=lambda: confirm_delete_student(tree, selected_item, student_id))
        details_button.config(state="normal", command=lambda: open_student_details(student_id))
        pdf_button.config(state="normal", command=lambda: generate_pdf_for_student(selected_student))
    else:
        edit_button.config(state="disabled")
        delete_button.config(state="disabled")
        details_button.config(state="disabled")
        pdf_button.config(state="disabled")

def confirm_generate_certificate(form_window, certificate_type, first_name, last_name, id_number, year):
    # Función para confirmar y generar el certificado
    generate_certificate(certificate_type, first_name, last_name, id_number, year)
    form_window.destroy()

def on_enter(e):
    e.widget['background'] = BUTTON_COLOR_HOVER

def on_leave(e):
    e.widget['background'] = BUTTON_COLOR

def on_enter(e):
    e.widget['background'] = BUTTON_COLOR_HOVER

def on_leave(e):
    e.widget['background'] = BUTTON_COLOR