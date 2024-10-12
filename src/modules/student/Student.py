import tkinter as tk
from constants.Colors import (BACKGROUND_COLOR, TITLE_COLOR, BUTTON_COLOR, BUTTON_TEXT_COLOR, BUTTON_COLOR_HOVER, ENTRY_BACKGROUND, ENTRY_FOREGROUND)
from constants.Texts import (STUDENT_TITLE_EDIT, GLOBAL_STUDENT_TITLE_ADD, GLOBAL_CONFIRM_DELETE, GLOBAL_TABLE_NIT, GLOBAL_TABLE_NAME, GLOBAL_BUTTON_SAVE, GLOBAL_BUTTON_CONFIRM, GLOBAL_BUTTON_CANCEL, GLOBAL_LAST_NAME, GLOBAL_AGE, GLOBAL_SEX, GLOBAL_ADDRESS, GLOBAL_COURSE, GLOBAL_PHONE)

def add_student(tree, nit, name, lastName, age, sex, address, course, phone, new_window):
    tree.insert("", "end", values=(nit, name, lastName, age, sex, address, course, phone))
    print(f"Nuevo estudiante agregado con cédula: {nit}, nombre: {name}, apellido: {lastName}")
    new_window.destroy()

def update_student(tree, selected_item, nit, name, lastName, age, sex, address, course, phone, new_window):
    tree.item(selected_item, values=(nit, name, lastName, age, sex, address, course, phone))
    print(f"Estudiante actualizado con cédula: {nit}, nombre: {name}, apellido: {lastName}")
    new_window.destroy()

def open_student_details(student_data):
    details_window = tk.Toplevel()
    details_window.title("Detalles del Estudiante")
    details_window.geometry("300x400")
    details_window.configure(bg=BACKGROUND_COLOR)

    fields = [
        (GLOBAL_TABLE_NIT, student_data[0] if len(student_data) > 0 else "N/A"),
        (GLOBAL_TABLE_NAME, student_data[1] if len(student_data) > 1 else "N/A"),
        (GLOBAL_LAST_NAME, student_data[2] if len(student_data) > 2 else "N/A"),
        (GLOBAL_AGE, student_data[3] if len(student_data) > 3 else "N/A"),
        (GLOBAL_SEX, student_data[4] if len(student_data) > 4 else "N/A"),
        (GLOBAL_ADDRESS, student_data[5] if len(student_data) > 5 else "N/A"),
        (GLOBAL_COURSE, student_data[6] if len(student_data) > 6 else "N/A"),
        (GLOBAL_PHONE, student_data[7] if len(student_data) > 7 else "N/A")
    ]

    for label_text, value in fields:
        label = tk.Label(details_window, text=f"{label_text}: {value}", bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=("Helvetica", 12))
        label.pack(pady=5)

    close_button = tk.Button(details_window, text="Cerrar", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, command=details_window.destroy)
    close_button.pack(pady=10)
    close_button.bind("<Enter>", on_enter)
    close_button.bind("<Leave>", on_leave)

def open_edit_student_form(tree, selected_item, student_data):
    new_window = tk.Toplevel()
    new_window.title(STUDENT_TITLE_EDIT)
    new_window.geometry("1200x400")
    new_window.configure(bg=BACKGROUND_COLOR)

    main_frame = tk.Frame(new_window, bg=BACKGROUND_COLOR)
    main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    # Lista de campos en el orden que deseas
    fields = [
        ("Cédula", GLOBAL_TABLE_NIT),
        ("Nombres", GLOBAL_TABLE_NAME),
        ("Apellidos", GLOBAL_LAST_NAME),
        ("Lugar de Nacimiento", 'Lugar de Nacimiento'),
        ("Nacionalidad", 'Nacionalidad'),
        ("Edad", GLOBAL_AGE),
        ("Día de Nacimiento", "Día"),
        ("Mes de Nacimiento", "Mes"),
        ("Año de Nacimiento", "Año"),
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

    entries = {}

    # Organizar los campos en una cuadrícula de tres columnas
    for i, (field, label_text) in enumerate(fields):
        row = i // 3  # Cada tres campos comenzamos una nueva fila
        col = i % 3   # Usamos el módulo para distribuir en 3 columnas

        label = tk.Label(main_frame, text=label_text, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
        label.grid(row=row, column=col * 2, padx=(10, 5), pady=5, sticky='e')

        entry = tk.Entry(main_frame, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
        entry.insert(0, student_data[i] if i < len(student_data) else "")
        entry.grid(row=row, column=(col * 2) + 1, padx=(0, 10), pady=5, sticky='w')

        entries[field] = entry

    # Botón de guardar
    save_button = tk.Button(new_window, text=GLOBAL_BUTTON_SAVE, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                            command=lambda: update_student(tree, selected_item, 
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
                                                           new_window))
    save_button.pack(pady=20)
    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)

    # Configurar columnas para que se expandan uniformemente
    for i in range(6):  # 3 columnas * 2 (etiqueta + entrada) = 6 columnas
        main_frame.columnconfigure(i, weight=1)

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

def on_enter(e):
    e.widget['background'] = BUTTON_COLOR_HOVER

def on_leave(e):
    e.widget['background'] = BUTTON_COLOR



def open_new_student_form(tree):
    new_window = tk.Toplevel()
    new_window.title(GLOBAL_STUDENT_TITLE_ADD)
    new_window.geometry("1200x400")
    new_window.configure(bg=BACKGROUND_COLOR)

    main_frame = tk.Frame(new_window, bg=BACKGROUND_COLOR)
    main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    # Lista de campos en el orden que deseas
    fields = [
        ("Cédula", GLOBAL_TABLE_NIT),
        ("Nombres", GLOBAL_TABLE_NAME),
        ("Apellidos", GLOBAL_LAST_NAME),
        ("Lugar de Nacimiento", 'Lugar de Nacimiento'),
        ("Nacionalidad", 'Nacionalidad'),
        ("Edad", GLOBAL_AGE),
        ("Día de Nacimiento", "Día"),
        ("Mes de Nacimiento", "Mes"),
        ("Año de Nacimiento", "Año"),
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

    entries = {}

    # Organizar los campos en una cuadrícula de tres columnas
    for i, (field, label_text) in enumerate(fields):
        row = i // 3  # Cada 3 campos en una nueva fila
        col = i % 3   # Distribuir en 3 columnas

        label = tk.Label(main_frame, text=label_text, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
        label.grid(row=row, column=col * 2, padx=(10, 5), pady=5, sticky='e')  # Etiqueta en la columna impar

        entry = tk.Entry(main_frame, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
        entry.grid(row=row, column=(col * 2) + 1, padx=(0, 10), pady=5, sticky='w')  # Entrada en la columna par

        entries[field] = entry

    # Botón de guardar
    save_button = tk.Button(new_window, text=GLOBAL_BUTTON_SAVE, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                            command=lambda: add_student(tree, 
                                                        entries["Cédula"].get(),
                                                        entries["Nombres"].get(),
                                                        entries["Apellidos"].get(),
                                                        entries["Edad"].get(),
                                                        entries["Sexo"].get(),
                                                        entries["Dirección"].get(),
                                                        entries["Año que cursa"].get(),
                                                        entries["Teléfono"].get(),
                                                        new_window))
    save_button.pack(pady=20)

    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)

    # Configurar columnas para que se expandan uniformemente
    for i in range(6):  # 3 columnas * 2 (etiqueta + entrada) = 6 columnas
        main_frame.columnconfigure(i, weight=1)