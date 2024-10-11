import tkinter as tk
from tkinter import ttk
from constants.Colors import (BACKGROUND_COLOR, TITLE_COLOR, BUTTON_COLOR, BUTTON_TEXT_COLOR, BUTTON_COLOR_HOVER, ENTRY_BACKGROUND, ENTRY_FOREGROUND)
from constants.Texts import (STUDENT_TITLE_EDIT, GLOBAL_STUDENT_TITLE_ADD, GLOBAL_CONFIRM_DELETE, GLOBAL_TABLE_NIT, GLOBAL_TABLE_NAME, GLOBAL_BUTTON_SAVE, GLOBAL_BUTTON_CONFIRM, GLOBAL_BUTTON_CANCEL, GLOBAL_LAST_NAME, GLOBAL_AGE, GLOBAL_SEX, GLOBAL_ADDRESS, GLOBAL_COURSE, GLOBAL_PHONE)

# Add new global text constants
GLOBAL_TABLE_NAME = "Nombres"
GLOBAL_BIRTH_PLACE = "Lugar de Nacimiento"
GLOBAL_BIRTH_DATE = "Fecha de Nacimiento"
GLOBAL_NATIONALITY = "Nacionalidad"
GLOBAL_PREVIOUS_SCHOOL = "Plantel de Procedencia"
GLOBAL_PENDING_SUBJECT = "Trae Materia Pendiente"
GLOBAL_WHICH_SUBJECT = "¿Cuál?"
GLOBAL_REPEATING = "Repite"
GLOBAL_WHICH_SUBJECTS = "¿Con Cuáles?"
GLOBAL_LIVES_WITH_PARENTS = "¿Vive con sus Padres?"
GLOBAL_STUDENT_EMAIL = "Correo Electrónico del Estudiante"
GLOBAL_RELIGION = "Religión"

def on_enter(event):
    event.widget['background'] = BUTTON_COLOR_HOVER

def on_leave(event):
    event.widget['background'] = BUTTON_COLOR

# La función on_click_action se puede definir según lo que necesites, aquí es un ejemplo básico.
def on_click_action(tree, edit_button, delete_button, details_button):
    print("Acción de clic realizada")

def add_student(tree, nit, first_name, last_name, birth_place, birth_day, birth_month, birth_year, age, nationality, previous_school, pending_subject, which_subject, address, repeating, which_subjects, lives_with_parents, email, religion, sex, course, phone, new_window):
    tree.insert("", "end", values=(nit, first_name, last_name, birth_place, f"{birth_day}/{birth_month}/{birth_year}", age, nationality, previous_school, pending_subject, which_subject, address, repeating, which_subjects, lives_with_parents, email, religion, sex, course, phone))
    print(f"Nuevo estudiante agregado con cédula: {nit}, nombre: {first_name}, apellido: {last_name}")
    new_window.destroy()

def update_student(tree, selected_item, nit, first_name, last_name, birth_place, birth_day, birth_month, birth_year, age, nationality, previous_school, pending_subject, which_subject, address, repeating, which_subjects, lives_with_parents, email, religion, sex, course, phone, new_window):
    tree.item(selected_item, values=(nit, first_name, last_name, birth_place, f"{birth_day}/{birth_month}/{birth_year}", age, nationality, previous_school, pending_subject, which_subject, address, repeating, which_subjects, lives_with_parents, email, religion, sex, course, phone))
    print(f"Estudiante actualizado con cédula: {nit}, nombre: {first_name}, apellido: {last_name}")
    new_window.destroy()

def open_student_details(student_data):
    details_window = tk.Toplevel()
    details_window.title("Detalles del Estudiante")
    details_window.geometry("400x600")
    details_window.configure(bg=BACKGROUND_COLOR)

    fields = [
        (GLOBAL_TABLE_NIT, student_data[0]),
        (GLOBAL_TABLE_NAME, student_data[1]),
        (GLOBAL_LAST_NAME, student_data[2]),
        (GLOBAL_BIRTH_PLACE, student_data[3]),
        (GLOBAL_BIRTH_DATE, student_data[4]),
        (GLOBAL_AGE, student_data[5]),
        (GLOBAL_NATIONALITY, student_data[6]),
        (GLOBAL_PREVIOUS_SCHOOL, student_data[7]),
        (GLOBAL_PENDING_SUBJECT, student_data[8]),
        (GLOBAL_WHICH_SUBJECT, student_data[9]),
        (GLOBAL_ADDRESS, student_data[10]),
        (GLOBAL_REPEATING, student_data[11]),
        (GLOBAL_WHICH_SUBJECTS, student_data[12]),
        (GLOBAL_LIVES_WITH_PARENTS, student_data[13]),
        (GLOBAL_STUDENT_EMAIL, student_data[14]),
        (GLOBAL_RELIGION, student_data[15]),
        (GLOBAL_SEX, student_data[16]),
        (GLOBAL_COURSE, student_data[17]),
        (GLOBAL_PHONE, student_data[18])
    ]

    for label_text, value in fields:
        label = tk.Label(details_window, text=f"{label_text}: {value}", bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=("Helvetica", 12))
        label.pack(pady=5)

    close_button = tk.Button(details_window, text="Cerrar", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, command=details_window.destroy)
    close_button.pack(pady=10)
    close_button.bind("<Enter>", on_enter)
    close_button.bind("<Leave>", on_leave)

def create_form_field(parent, row, column, label_text, entry_var):
    label = tk.Label(parent, text=label_text, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
    label.grid(row=row, column=column*2, sticky="e", padx=5, pady=5)
    entry = tk.Entry(parent, textvariable=entry_var, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
    entry.grid(row=row, column=column*2+1, sticky="w", padx=5, pady=5)
    return entry

def open_new_student_form(tree):
    new_window = tk.Toplevel()
    new_window.title(GLOBAL_STUDENT_TITLE_ADD)
    new_window.geometry("500x500")
    new_window.configure(bg=BACKGROUND_COLOR)

    main_frame = tk.Frame(new_window, bg=BACKGROUND_COLOR)
    main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    # Lista de campos en el orden que deseas
    fields = [
        ("Cédula", GLOBAL_TABLE_NIT),
        ("Nombres", GLOBAL_TABLE_NAME),
        ("Apellidos", GLOBAL_LAST_NAME),
        ("Lugar de Nacimiento", GLOBAL_BIRTH_PLACE),
        ("Nacionalidad", GLOBAL_NATIONALITY),
        ("Edad", GLOBAL_AGE),
        ("Día de Nacimiento", "Día"),
        ("Mes de Nacimiento", "Mes"),
        ("Año de Nacimiento", "Año"),
        ("Plantel de Procedencia", GLOBAL_PREVIOUS_SCHOOL),
        ("Trae Materia Pendiente", GLOBAL_PENDING_SUBJECT),
        ("¿Cuál?", GLOBAL_WHICH_SUBJECT),
        ("Dirección", GLOBAL_ADDRESS),
        ("Repite", GLOBAL_REPEATING),
        ("¿Con Cuáles?", GLOBAL_WHICH_SUBJECTS),
        ("¿Vive con sus Padres?", GLOBAL_LIVES_WITH_PARENTS),
        ("Correo Electrónico", GLOBAL_STUDENT_EMAIL),
        ("Religión", GLOBAL_RELIGION),
        ("Sexo", GLOBAL_SEX),
        ("Año que cursa", GLOBAL_COURSE),
        ("Teléfono", GLOBAL_PHONE)
    ]

    entries = {}

    # Iterar sobre los campos y colocarlos en una cuadrícula de tres columnas
    for i, (field, label_text) in enumerate(fields):
        row = i // 3  # Cada tres campos comenzamos una nueva fila
        col = i % 3    # Usamos el módulo para la columna (0, 1, 2)

        # Crear etiqueta
        label = tk.Label(main_frame, text=label_text, bg=BACKGROUND_COLOR, fg=TITLE_COLOR, anchor='e')
        label.grid(row=row, column=col, padx=(10, 5), pady=5, sticky='e')

        # Crear entrada
        entry = tk.Entry(main_frame, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
        entry.grid(row=row, column=col + 1, padx=(0, 10), pady=5, sticky='w')

        entries[field] = entry

    # Botón de guardar
    save_button = tk.Button(new_window, text=GLOBAL_BUTTON_SAVE, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat",
                            command=lambda: add_student(tree,
                                                        entries["Cédula"].get(),
                                                        entries["Nombres"].get(),
                                                        entries["Apellidos"].get(),
                                                        entries["Lugar de Nacimiento"].get(),
                                                        entries["Día de Nacimiento"].get(),
                                                        entries["Mes de Nacimiento"].get(),
                                                        entries["Año de Nacimiento"].get(),
                                                        entries["Edad"].get(),
                                                        entries["Nacionalidad"].get(),
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
                                                        new_window))
    save_button.pack(pady=20)

    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)

    # Configurar columnas para que se expandan uniformemente
    for i in range(6):  # 3 columnas * 2 (etiqueta + campo) = 6 columnas
        main_frame.columnconfigure(i, weight=1)

    # Configurar filas para que se expandan
    main_frame.rowconfigure(len(fields) // 3, weight=1)
    
"""  
def open_new_student_form(tree):
    new_window = tk.Toplevel()
    new_window.title(GLOBAL_STUDENT_TITLE_ADD)
    new_window.geometry("500x800")
    new_window.configure(bg=BACKGROUND_COLOR)

    fields = [
        ("Cédula", GLOBAL_TABLE_NIT),
        ("Nombres", GLOBAL_TABLE_NAME),
        ("Apellidos", GLOBAL_LAST_NAME),
        ("Lugar de Nacimiento", GLOBAL_BIRTH_PLACE),
        ("Día de Nacimiento", "Día"),
        ("Mes de Nacimiento", "Mes"),
        ("Año de Nacimiento", "Año"),
        ("Edad", GLOBAL_AGE),
        ("Nacionalidad", GLOBAL_NATIONALITY),
        ("Plantel de Procedencia", GLOBAL_PREVIOUS_SCHOOL),
        ("Trae Materia Pendiente", GLOBAL_PENDING_SUBJECT),
        ("¿Cuál?", GLOBAL_WHICH_SUBJECT),
        ("Dirección", GLOBAL_ADDRESS),
        ("Repite", GLOBAL_REPEATING),
        ("¿Con Cuáles?", GLOBAL_WHICH_SUBJECTS),
        ("¿Vive con sus Padres?", GLOBAL_LIVES_WITH_PARENTS),
        ("Correo Electrónico", GLOBAL_STUDENT_EMAIL),
        ("Religión", GLOBAL_RELIGION),
        ("Sexo", GLOBAL_SEX),
        ("Año que cursa", GLOBAL_COURSE),
        ("Teléfono", GLOBAL_PHONE)
    ]

    entries = {}

    for field, label_text in fields:
        label = tk.Label(new_window, text=label_text, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
        label.pack(pady=5)
        entry = tk.Entry(new_window, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
        entry.pack(pady=5)
        entries[field] = entry

    save_button = tk.Button(new_window, text=GLOBAL_BUTTON_SAVE, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                            command=lambda: add_student(tree, 
                                                        entries["Cédula"].get(),
                                                        entries["Nombres"].get(),
                                                        entries["Apellidos"].get(),
                                                        entries["Lugar de Nacimiento"].get(),
                                                        entries["Día de Nacimiento"].get(),
                                                        entries["Mes de Nacimiento"].get(),
                                                        entries["Año de Nacimiento"].get(),
                                                        entries["Edad"].get(),
                                                        entries["Nacionalidad"].get(),
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
                                                        new_window))
    save_button.pack(pady=10)

    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)

# The rest of the functions (on_enter, on_leave, on_click_action, confirm_delete_student) remain unchanged
"""