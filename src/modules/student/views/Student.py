import tkinter as tk
from tkinter import ttk
from constants.Colors import (BACKGROUND_COLOR, TITLE_COLOR, BUTTON_COLOR, BUTTON_TEXT_COLOR, BUTTON_COLOR_HOVER, ENTRY_BACKGROUND, ENTRY_FOREGROUND)
from constants.Texts import (STUDENT_TITLE_EDIT, GLOBAL_STUDENT_TITLE_ADD, GLOBAL_CONFIRM_DELETE, GLOBAL_TABLE_NIT, GLOBAL_TABLE_NAME, GLOBAL_BUTTON_SAVE, GLOBAL_BUTTON_CONFIRM, GLOBAL_BUTTON_CANCEL, GLOBAL_LAST_NAME, GLOBAL_AGE, GLOBAL_SEX, GLOBAL_ADDRESS, GLOBAL_COURSE, GLOBAL_PHONE)

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
    ("Nombre del Familiar", "Nombre Familiar"),
    ("Cédula del Familiar", "Cédula Familiar")
]

representative_fields = [
    ("Nombre del Representante", "Nombre Representante"),
    ("Cédula del Representante", "Cédula Representante")
]

# Actions

def add_student(tree, nit, name, lastName, birth_place,
                nationality, age, birth_day, birth_month, birth_year,
                previous_school, pending_subject, which_subject, address, 
                repeating, which_subjects, lives_with_parents, email, religion, sex,
                course, phone, family_name, family_nit, representative_name, representative_nit, new_window):

    tree.insert("", "end", values=(nit, name, lastName, birth_place, nationality, age, birth_day, birth_month, birth_year,
                                     previous_school, pending_subject, which_subject, address, 
                                     repeating, which_subjects, lives_with_parents, email, religion, sex, course, phone, family_name, family_nit, representative_name, representative_nit))
    print(f"Nuevo estudiante agregado con cédula: {nit}, nombre: {name}, apellido: {lastName}")
    new_window.destroy()

def update_student(tree, selected_item, 
                   nit, name, lastName, birth_place,
                   nationality, age, birth_day, birth_month, birth_year,
                   previous_school, pending_subject, which_subject, address, 
                   repeating, which_subjects, lives_with_parents, email, religion, sex,
                   course, phone, family_name, family_nit, representative_name, representative_nit, new_window):
    
    tree.item(selected_item, values=(nit, name, lastName, birth_place, nationality, age, birth_day, birth_month, birth_year,
                                     previous_school, pending_subject, which_subject, address, 
                                     repeating, which_subjects, lives_with_parents, email, religion, sex, course, phone, family_name, family_nit, representative_name, representative_nit))
    print(f"Estudiante actualizado con cédula: {nit}, nombre: {name}, apellido: {lastName}")
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
        tree.delete(selected_item)
        print(f"Estudiante con cédula {student_id} borrado")
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

# Opens Windows

def open_new_student_form(tree):
    new_window = tk.Toplevel()
    new_window.title(GLOBAL_STUDENT_TITLE_ADD)
    new_window.geometry("1200x425")
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
        label = tk.Label(family_frame, text=label_text, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
        label.grid(row=i, column=0, padx=(10, 5), pady=5, sticky='e')

        entry = tk.Entry(family_frame, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
        entry.grid(row=i, column=1, padx=(0, 10), pady=5, sticky='w')
        entries[field] = entry


    for i, (field, label_text) in enumerate(representative_fields):
        label = tk.Label(representative_frame, text=label_text, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
        label.grid(row=i, column=0, padx=(10, 5), pady=5, sticky='e')

        entry = tk.Entry(representative_frame, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
        entry.grid(row=i, column=1, padx=(0, 10), pady=5, sticky='w')
        entries[field] = entry

    # Botón de guardar
    save_button = tk.Button(new_window, text=GLOBAL_BUTTON_SAVE, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                            command=lambda: add_student(tree, 
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
                                                        entries["Nombre del Familiar"].get(),
                                                        entries["Cédula del Familiar"].get(),
                                                        entries["Nombre del Representante"].get(),
                                                        entries["Cédula del Representante"].get(),
                                                        new_window))
    save_button.pack(pady=20)
    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)

def open_edit_student_form(tree, selected_item, student_data):
    new_window = tk.Toplevel()
    new_window.title(STUDENT_TITLE_EDIT)
    new_window.geometry("1200x500")
    new_window.configure(bg=BACKGROUND_COLOR)

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

    entries = {}

    # Organizar los campos en la pestaña de Datos del Estudiante
    for i, (field, label_text) in enumerate(fields):
        row = i // 3
        col = i % 3

        label = tk.Label(student_frame, text=label_text, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
        label.grid(row=row, column=col * 2, padx=(10, 5), pady=5, sticky='e')

        entry = tk.Entry(student_frame, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
        entry.insert(0, student_data[i] if i < len(student_data) else "")
        entry.grid(row=row, column=(col * 2) + 1, padx=(0, 10), pady=5, sticky='w')
        entries[field] = entry

    # Organizar los campos en la pestaña de Datos del Familiar
    for i, (field, label_text) in enumerate(family_fields):
        label = tk.Label(family_frame, text=label_text, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
        label.grid(row=i, column=0, padx=(10, 5), pady=5, sticky='e')

        entry = tk.Entry(family_frame, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
        entry.insert(0, student_data[len(fields) + i] if len(student_data) > len(fields) + i else "")
        entry.grid(row=i, column=1, padx=(0, 10), pady=5, sticky='w')
        entries[field] = entry

    # Organizar los campos en la pestaña de Datos del Representante
    for i, (field, label_text) in enumerate(representative_fields):
        label = tk.Label(representative_frame, text=label_text, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
        label.grid(row=i, column=0, padx=(10, 5), pady=5, sticky='e')

        entry = tk.Entry(representative_frame, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
        entry.insert(0, student_data[len(fields) + len(family_fields) + i] if len(student_data) > len(fields) + len(family_fields) + i else "")
        entry.grid(row=i, column=1, padx=(0, 10), pady=5, sticky='w')
        entries[field] = entry

    # Botón de guardar
    save_button = tk.Button(new_window, text=GLOBAL_BUTTON_SAVE, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                            command=lambda: update_student(
                                tree, selected_item, 
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
                                entries["Nombre del Familiar"].get(),
                                entries["Cédula del Familiar"].get(),
                                entries["Nombre del Representante"].get(),
                                entries["Cédula del Representante"].get(),
                                new_window))

    save_button.pack(pady=20)
    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)

def open_student_details(student_data):
    details_window = tk.Toplevel()
    details_window.title("Detalles del Estudiante")
    details_window.geometry("600x500")
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

    # Mostrar campos en la pestaña de Datos del Estudiante
    for i, (field, label_text) in enumerate(fields):
        row = i // 3
        col = i % 3

        label = tk.Label(student_frame, text=f"{label_text}:", bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=("Helvetica", 12))
        label.grid(row=row, column=col * 2, padx=(10, 5), pady=5, sticky='e')

        value = student_data[i] if i < len(student_data) else "N/A"
        value_label = tk.Label(student_frame, text=value, bg=BACKGROUND_COLOR, fg=ENTRY_FOREGROUND, font=("Helvetica", 12))
        value_label.grid(row=row, column=(col * 2) + 1, padx=(0, 10), pady=5, sticky='w')

    # Mostrar campos en la pestaña de Datos del Familiar
    for i, (field, label_text) in enumerate(family_fields):
        label = tk.Label(family_frame, text=f"{label_text}:", bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=("Helvetica", 12))
        label.grid(row=i, column=0, padx=(10, 5), pady=5, sticky='e')

        value = student_data[len(fields) + i] if len(student_data) > len(fields) + i else "N/A"
        value_label = tk.Label(family_frame, text=value, bg=BACKGROUND_COLOR, fg=ENTRY_FOREGROUND, font=("Helvetica", 12))
        value_label.grid(row=i, column=1, padx=(0, 10), pady=5, sticky='w')

    # Mostrar campos en la pestaña de Datos del Representante
    for i, (field, label_text) in enumerate(representative_fields):
        label = tk.Label(representative_frame, text=f"{label_text}:", bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=("Helvetica", 12))
        label.grid(row=i, column=0, padx=(10, 5), pady=5, sticky='e')

        value = student_data[len(fields) + len(family_fields) + i] if len(student_data) > len(fields) + len(family_fields) + i else "N/A"
        value_label = tk.Label(representative_frame, text=value, bg=BACKGROUND_COLOR, fg=ENTRY_FOREGROUND, font=("Helvetica", 12))
        value_label.grid(row=i, column=1, padx=(0, 10), pady=5, sticky='w')

    close_button = tk.Button(details_window, text="Cerrar", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, command=details_window.destroy)
    close_button.pack(pady=10)
    close_button.bind("<Enter>", on_enter)
    close_button.bind("<Leave>", on_leave)

# Handles

def on_click_action(tree, edit_button, delete_button, details_button):
    selected_item = tree.selection()
    if selected_item:
        selected_student = tree.item(selected_item, 'values')
        edit_button.config(state="normal", command=lambda: open_edit_student_form(tree, selected_item, selected_student))
        delete_button.config(state="normal", command=lambda: confirm_delete_student(tree, selected_item, selected_student[0]))
        details_button.config(state="normal", command=lambda: open_student_details(selected_student))
    else:
        edit_button.config(state="disabled")
        delete_button.config(state="disabled")
        details_button.config(state="disabled")

def on_enter(e):
    e.widget['background'] = BUTTON_COLOR_HOVER

def on_leave(e):
    e.widget['background'] = BUTTON_COLOR

def on_enter(e):
    e.widget['background'] = BUTTON_COLOR_HOVER

def on_leave(e):
    e.widget['background'] = BUTTON_COLOR
