import tkinter as tk
from constants.Colors import (BACKGROUND_COLOR, TITLE_COLOR, BUTTON_COLOR, BUTTON_TEXT_COLOR, BUTTON_COLOR_HOVER, ENTRY_BACKGROUND, ENTRY_FOREGROUND)
from constants.Texts import (STUDENT_TITLE_EDIT, GLOBAL_STUDENT_TITLE_ADD, GLOBAL_CONFIRM_DELETE, GLOBAL_TABLE_NIT, GLOBAL_TABLE_NAME, GLOBAL_BUTTON_SAVE, GLOBAL_BUTTON_CONFIRM, GLOBAL_BUTTON_CANCEL)

def add_student(tree, cedula, nombre, apellido, edad, sexo, direccion, ano_curso, telefono, new_window):
    tree.insert("", "end", values=(cedula, nombre, apellido, edad, sexo, direccion, ano_curso, telefono))
    print(f"Nuevo estudiante agregado con cédula: {cedula}, nombre: {nombre}, apellido: {apellido}")
    new_window.destroy()

def update_student(tree, selected_item, cedula, nombre, apellido, edad, sexo, direccion, ano_curso, telefono, new_window):
    tree.item(selected_item, values=(cedula, nombre, apellido, edad, sexo, direccion, ano_curso, telefono))
    print(f"Estudiante actualizado con cédula: {cedula}, nombre: {nombre}, apellido: {apellido}")
    new_window.destroy()

def open_edit_student_form(tree, selected_item, student_data):
    new_window = tk.Toplevel()
    new_window.title(STUDENT_TITLE_EDIT)
    new_window.geometry("400x500")
    new_window.configure(bg=BACKGROUND_COLOR)

    fields = [
        ("Cédula", GLOBAL_TABLE_NIT),
        ("Nombre", GLOBAL_TABLE_NAME),
        ("Apellido", "Apellido"),
        ("Edad", "Edad"),
        ("Sexo", "Sexo"),
        ("Dirección", "Dirección"),
        ("Año que cursa", "Año que cursa"),
        ("Teléfono", "Teléfono")
    ]

    entries = {}

    for i, (field, label_text) in enumerate(fields):
        label = tk.Label(new_window, text=label_text, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
        label.pack(pady=5)
        entry = tk.Entry(new_window, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
        entry.insert(0, student_data[i] if i < len(student_data) else "")
        entry.pack(pady=5)
        entries[field] = entry

    save_button = tk.Button(new_window, text=GLOBAL_BUTTON_SAVE, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                            command=lambda: update_student(tree, selected_item, 
                                                           entries["Cédula"].get(),
                                                           entries["Nombre"].get(),
                                                           entries["Apellido"].get(),
                                                           entries["Edad"].get(),
                                                           entries["Sexo"].get(),
                                                           entries["Dirección"].get(),
                                                           entries["Año que cursa"].get(),
                                                           entries["Teléfono"].get(),
                                                           new_window))
    save_button.pack(pady=10)

    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)

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

def on_click_action(tree, edit_button, delete_button):
    selected_item = tree.selection()
    if selected_item:
        selected_student = tree.item(selected_item, 'values')
        student_id = selected_student[0]

        edit_button.config(state="normal", command=lambda: open_edit_student_form(tree, selected_item, selected_student))
        delete_button.config(state="normal", command=lambda: confirm_delete_student(tree, selected_item, student_id))

def open_new_student_form(tree):
    new_window = tk.Toplevel()
    new_window.title(GLOBAL_STUDENT_TITLE_ADD)
    new_window.geometry("400x500")
    new_window.configure(bg=BACKGROUND_COLOR)

    fields = [
        ("Cédula", GLOBAL_TABLE_NIT),
        ("Nombre", GLOBAL_TABLE_NAME),
        ("Apellido", "Apellido"),
        ("Edad", "Edad"),
        ("Sexo", "Sexo"),
        ("Dirección", "Dirección"),
        ("Año que cursa", "Año que cursa"),
        ("Teléfono", "Teléfono")
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
                                                        entries["Nombre"].get(),
                                                        entries["Apellido"].get(),
                                                        entries["Edad"].get(),
                                                        entries["Sexo"].get(),
                                                        entries["Dirección"].get(),
                                                        entries["Año que cursa"].get(),
                                                        entries["Teléfono"].get(),
                                                        new_window))
    save_button.pack(pady=10)

    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)
    
    