import tkinter as tk
from constants.Colors import (BACKGROUND_COLOR, TITLE_COLOR, BUTTON_COLOR, BUTTON_TEXT_COLOR, BUTTON_COLOR_HOVER, ENTRY_BACKGROUND, ENTRY_FOREGROUND)
from constants.Texts import (GLOBAL_TITLE_EDIT, TEACHER_TITLE_ADD, GLOBAL_CONFIRM_DELETE, GLOBAL_TABLE_NIT, GLOBAL_TABLE_NAME, GLOBAL_BUTTON_SAVE, GLOBAL_BUTTON_CONFIRM, GLOBAL_BUTTON_CANCEL, GLOBAL_LAST_NAME, GLOBAL_AGE, GLOBAL_SEX, GLOBAL_ADDRESS, GLOBAL_SUBJECT, GLOBAL_PHONE)

def add_teacher(tree, nit, name, lastName, age, sex, address, subject, phone, new_window):
    tree.insert("", "end", values=(nit, name, lastName, age, sex, address, subject, phone))
    print(f"Nuevo docente agregado con cédula: {nit}, nombre: {name}, apellido: {lastName}")
    new_window.destroy()

def update_teacher(tree, selected_item, nit, name, lastName, age, sex, address, subject, phone, new_window):
    tree.item(selected_item, values=(nit, name, lastName, age, sex, address, subject, phone))
    print(f"Docente actualizado con cédula: {nit}, nombre: {name}, apellido: {lastName}")
    new_window.destroy()

def open_teacher_details(teacher_data):
    details_window = tk.Toplevel()
    details_window.title("Detalles del Docente")
    details_window.geometry("300x200")
    details_window.configure(bg=BACKGROUND_COLOR)

    fields = [
        (GLOBAL_TABLE_NIT, teacher_data[0] if len(teacher_data) > 0 else "N/A"),
        (GLOBAL_TABLE_NAME, teacher_data[1] if len(teacher_data) > 1 else "N/A"),
        (GLOBAL_LAST_NAME, teacher_data[2] if len(teacher_data) > 2 else "N/A"),
        (GLOBAL_AGE, teacher_data[3] if len(teacher_data) > 3 else "N/A"),
        (GLOBAL_SEX, teacher_data[4] if len(teacher_data) > 4 else "N/A"),
        (GLOBAL_ADDRESS, teacher_data[5] if len(teacher_data) > 5 else "N/A"),
        (GLOBAL_SUBJECT, teacher_data[6] if len(teacher_data) > 6 else "N/A"),
        (GLOBAL_PHONE, teacher_data[7] if len(teacher_data) > 7 else "N/A")
    ]

    for i, (label_text, value) in enumerate(fields):
        row = i // 2
        col = i % 2

        label = tk.Label(details_window, text=f"{label_text}: {value}", bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=("Helvetica", 12))
        label.grid(row=row, column=col * 2, padx=(10, 5), pady=5, sticky='e')

    close_button = tk.Button(details_window, text="Cerrar", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, command=details_window.destroy)
    close_button.grid(row=(len(fields) // 2) + 1, column=1, pady=10, columnspan=3)

    close_button.bind("<Enter>", on_enter)
    close_button.bind("<Leave>", on_leave)


def open_edit_teacher_form(tree, selected_item, teacher_data):
    new_window = tk.Toplevel()
    new_window.title(GLOBAL_TITLE_EDIT)
    new_window.geometry("600x200")
    new_window.configure(bg=BACKGROUND_COLOR)

    fields = [
        ("Cédula", GLOBAL_TABLE_NIT),
        ("Nombre", GLOBAL_TABLE_NAME),
        ("Apellido", GLOBAL_LAST_NAME),
        ("Edad", GLOBAL_AGE),
        ("Sexo", GLOBAL_SEX),
        ("Dirección", GLOBAL_ADDRESS),
        ("Asignatura", GLOBAL_SUBJECT),
        ("Teléfono", GLOBAL_PHONE)
    ]

    entries = {}

    for i, (field, label_text) in enumerate(fields):
        row = i // 2
        col = i % 2

        label = tk.Label(new_window, text=label_text, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
        label.grid(row=row, column=col * 2, padx=(10, 5), pady=5, sticky='e')

        entry = tk.Entry(new_window, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
        entry.insert(0, teacher_data[i] if i < len(teacher_data) else "")
        entry.grid(row=row, column=(col * 2) + 1, padx=(0, 10), pady=5, sticky='w')
        entries[field] = entry

    save_button = tk.Button(new_window, text=GLOBAL_BUTTON_SAVE, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                            command=lambda: update_teacher(tree, selected_item, 
                                                           entries[GLOBAL_TABLE_NIT].get(),
                                                           entries[GLOBAL_TABLE_NAME].get(),
                                                           entries[GLOBAL_LAST_NAME].get(),
                                                           entries[GLOBAL_AGE].get(),
                                                           entries[GLOBAL_SEX].get(),
                                                           entries[GLOBAL_ADDRESS].get(),
                                                           entries[GLOBAL_SUBJECT].get(),
                                                           entries[GLOBAL_PHONE].get(),
                                                           new_window))
    save_button.grid(row=(len(fields) // 2) + 1, column=1, pady=10, columnspan=3)

    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)


def confirm_delete_teacher(tree, selected_item, teacher_id):
    new_window = tk.Toplevel()
    new_window.title(GLOBAL_CONFIRM_DELETE)
    new_window.geometry("300x150")
    new_window.configure(bg=BACKGROUND_COLOR)

    label_message = tk.Label(new_window, text=f"¿Estás seguro de que deseas borrar al docente con cédula {teacher_id}?", 
                             bg=BACKGROUND_COLOR, fg=TITLE_COLOR, wraplength=250)
    label_message.pack(pady=10)

    def delete_confirmed():
        tree.delete(selected_item)
        print(f"Docente con cédula {teacher_id} borrado")
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

def on_click_action(tree, edit_button, delete_button, details_button, attendance_button):
    selected_item = tree.selection()
    if selected_item:
        selected_teacher = tree.item(selected_item, 'values')
        edit_button.config(state="normal", command=lambda: open_edit_teacher_form(tree, selected_item, selected_teacher))
        delete_button.config(state="normal", command=lambda: confirm_delete_teacher(tree, selected_item, selected_teacher[0]))
        details_button.config(state="normal", command=lambda: open_teacher_details(selected_teacher))
        attendance_button.config(state="normal", command=lambda: open_attendance_form(tree, selected_item, selected_teacher))
    else:
        edit_button.config(state="disabled")
        delete_button.config(state="disabled")
        details_button.config(state="disabled")
        attendance_button.config(state="disabled")

def open_new_teacher_form(tree):
    new_window = tk.Toplevel()
    new_window.title(TEACHER_TITLE_ADD)
    new_window.geometry("600x200")
    new_window.configure(bg=BACKGROUND_COLOR)

    fields = [
        ("Cédula", GLOBAL_TABLE_NIT),
        ("Nombre", GLOBAL_TABLE_NAME),
        ("Apellido", GLOBAL_LAST_NAME),
        ("Edad", GLOBAL_AGE),
        ("Sexo", GLOBAL_SEX),
        ("Dirección", GLOBAL_ADDRESS),
        ("Curso", GLOBAL_SUBJECT),
        ("Teléfono", GLOBAL_PHONE)
    ]

    entries = {}

    for i, (field, label_text) in enumerate(fields):
        row = i // 2
        col = i % 2

        label = tk.Label(new_window, text=label_text, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
        label.grid(row=row, column=col * 2, padx=(10, 5), pady=5, sticky='e')

        entry = tk.Entry(new_window, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
        entry.grid(row=row, column=(col * 2) + 1, padx=(0, 10), pady=5, sticky='w')
        entries[field] = entry

    save_button = tk.Button(new_window, text=GLOBAL_BUTTON_SAVE, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                            command=lambda: add_teacher(tree, 
                                                        entries[GLOBAL_TABLE_NIT].get(),
                                                        entries[GLOBAL_TABLE_NAME].get(),
                                                        entries[GLOBAL_LAST_NAME].get(),
                                                        entries[GLOBAL_AGE].get(),
                                                        entries[GLOBAL_SEX].get(),
                                                        entries[GLOBAL_ADDRESS].get(),
                                                        entries[GLOBAL_SUBJECT].get(),
                                                        entries[GLOBAL_PHONE].get(),
                                                        new_window))
    save_button.grid(row=(len(fields) // 1) + 1, column=1, pady=10, columnspan=3)

    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)


def open_attendance_form(tree, selected_item, teacher_data):
    new_window = tk.Toplevel()
    new_window.title("Gestionar Asistencia")
    new_window.geometry("200x125")
    new_window.configure(bg=BACKGROUND_COLOR)
    
    message_label = tk.Label(new_window, text="¿El profesor asistió hoy?", bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=("Helvetica", 12))
    message_label.pack(pady=10)
    
    def mark_attendance(attended):
        attendance_status = "Sí" if attended else "No"
        teacher_data_list = list(teacher_data)
        teacher_data_list.append(attendance_status)
        
        # Actualiza la columna de asistencia
        tree.item(selected_item, values=teacher_data_list)
        
        print(f"Asistencia del profesor {teacher_data[1]} marcada como: {attendance_status}")
        new_window.destroy()
    
    # Botón para "Sí"
    yes_button = tk.Button(new_window, text="Sí", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, 
                           command=lambda: mark_attendance(True))
    yes_button.pack(side="left", padx=20, pady=20)
    yes_button.bind("<Enter>", on_enter)
    yes_button.bind("<Leave>", on_leave)
    
    # Botón para "No"
    no_button = tk.Button(new_window, text="No", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, 
                          command=lambda: mark_attendance(False))
    no_button.pack(side="right", padx=20, pady=20)
    no_button.bind("<Enter>", on_enter)
    no_button.bind("<Leave>", on_leave)

def on_enter(e):
    e.widget['background'] = BUTTON_COLOR_HOVER

def on_leave(e):
    e.widget['background'] = BUTTON_COLOR