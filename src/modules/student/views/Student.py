import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
from api.controllers.studentController import add_student_with_relations, delete_student, fetch_student_details, update_student_with_relations
from constants.Colors import (BACKGROUND_COLOR, TITLE_COLOR, BUTTON_COLOR, BUTTON_TEXT_COLOR, BUTTON_COLOR_HOVER, ENTRY_BACKGROUND, ENTRY_FOREGROUND)
from constants.Texts import (STUDENT_TITLE_EDIT, GLOBAL_STUDENT_TITLE_ADD, GLOBAL_CONFIRM_DELETE, GLOBAL_TABLE_NIT, GLOBAL_TABLE_NAME, GLOBAL_BUTTON_SAVE, GLOBAL_BUTTON_CONFIRM, GLOBAL_BUTTON_CANCEL, GLOBAL_LAST_NAME, GLOBAL_AGE, GLOBAL_SEX, GLOBAL_ADDRESS, GLOBAL_COURSE, GLOBAL_PHONE)
from src.modules.records.Records import generate_certificate

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


def add_student(tree,
                nit, name, lastName, birth_place, nationality, age, birth_day,
                birth_month, birth_year, previous_school, pending_subject, which_subject, address, repeating,
                which_subjects, lives_with_parents, email, religion, sex, course, phone, 

                name_of_parent, name_of_mother, nit_of_parent, nit_of_mother, phone_of_parent,
                phone_of_mother, office_of_parent, office_of_mother, email_of_parent, email_of_mother,

                name_of_representative, nit_of_representative, office_of_representative, relationship_to_student, 
                address_of_house, phone_of_house, phone_of_work, phone_of_cellular, email_of_representative, 
                in_case_of_no_acuity_to_meeting_or_delivery_of_bill_authorized_to, authorized_person_id,

                new_window):

    student_data = (
        nit, name, lastName, birth_place, nationality, age, birth_day,
        birth_month, birth_year, previous_school, pending_subject, which_subject, address, repeating,
        which_subjects, lives_with_parents, email, religion, sex, course, phone
    )

    family_data = (
        name_of_parent, name_of_mother, nit_of_parent, nit_of_mother, 
        phone_of_parent, phone_of_mother, office_of_parent, office_of_mother, 
        email_of_parent, email_of_mother
    )

    representative_data = (
        name_of_representative, nit_of_representative, office_of_representative, relationship_to_student, 
        address_of_house, phone_of_house, phone_of_work, phone_of_cellular, 
        email_of_representative, in_case_of_no_acuity_to_meeting_or_delivery_of_bill_authorized_to, authorized_person_id
    )

    success, message = add_student_with_relations(student_data, family_data, representative_data)
    
    if success:
        messagebox.showinfo("Registro Exitoso", message)
        tree.insert("", "end", values=student_data)
    else:
        messagebox.showerror("Error", message)
    
    new_window.destroy()

def update_student(tree, selected_item, student_id,
                   nit, name, lastName, birth_place, nationality, age, birth_day,
                   birth_month, birth_year, previous_school, pending_subject, which_subject, address, repeating,
                   which_subjects, lives_with_parents, email, religion, sex, course, phone,
                   name_of_parent, name_of_mother, nit_of_parent, nit_of_mother, phone_of_parent,
                   phone_of_mother, office_of_parent, office_of_mother, email_of_parent, email_of_mother,
                   name_of_representative, nit_of_representative, office_of_representative, relationship_to_student, 
                   address_of_house, phone_of_house, phone_of_work, phone_of_cellular, email_of_representative, 
                   in_case_of_no_acuity_to_meeting_or_delivery_of_bill_authorized_to, authorized_person_id,
                   new_window):

    student_data = (
        nit, name, lastName, birth_place, nationality, age, birth_day,
        birth_month, birth_year, previous_school, pending_subject, which_subject, address, repeating,
        which_subjects, lives_with_parents, email, religion, sex, course, phone
    )

    family_data = (
        name_of_parent, name_of_mother, nit_of_parent, nit_of_mother, 
        phone_of_parent, phone_of_mother, office_of_parent, office_of_mother, 
        email_of_parent, email_of_mother
    )

    representative_data = (
        name_of_representative, nit_of_representative, office_of_representative, relationship_to_student, 
        address_of_house, phone_of_house, phone_of_work, phone_of_cellular, 
        email_of_representative, in_case_of_no_acuity_to_meeting_or_delivery_of_bill_authorized_to, authorized_person_id
    )

    success, message = update_student_with_relations(student_id, student_data, family_data, representative_data)
    
    if success:
        messagebox.showinfo("Actualización Exitosa", message)
        tree.item(selected_item, values=(nit, name, lastName, birth_place, nationality, age, birth_day, 
                                         birth_month, birth_year, previous_school, pending_subject, which_subject, 
                                         address, repeating, which_subjects, lives_with_parents, email, religion, 
                                         sex, course, phone,
                                         
                                         name_of_parent, name_of_mother, nit_of_parent, nit_of_mother,
                                         phone_of_parent, phone_of_mother, office_of_parent, office_of_mother, 
                                         email_of_parent, email_of_mother,
                                         
                                         name_of_representative, nit_of_representative, office_of_representative, relationship_to_student,
                                         address_of_house, phone_of_house, phone_of_work, phone_of_cellular, 
                                         email_of_representative, in_case_of_no_acuity_to_meeting_or_delivery_of_bill_authorized_to,
                                         authorized_person_id
                                         ))
    else:
        messagebox.showerror("Error", message)
    
    new_window.destroy()

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

def generate_pdf_for_student(student_data):
    first_name = student_data[1]
    last_name = student_data[2]
    id_number = student_data[0]
    year = student_data[20]
    certificate_type = "Estudio"
    behavior = "Excelente" if certificate_type == "Buen Comportamiento" else None

    generate_certificate(certificate_type, first_name, last_name, id_number, year, behavior)
    
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

# Handles

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

def on_enter(e):
    e.widget['background'] = BUTTON_COLOR_HOVER

def on_leave(e):
    e.widget['background'] = BUTTON_COLOR

def on_enter(e):
    e.widget['background'] = BUTTON_COLOR_HOVER

def on_leave(e):
    e.widget['background'] = BUTTON_COLOR
