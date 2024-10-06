import tkinter as tk
from constants.Colors import (
    BACKGROUND_COLOR, TITLE_COLOR, 
    BUTTON_COLOR, BUTTON_TEXT_COLOR, BUTTON_COLOR_HOVER,
    ENTRY_BACKGROUND, ENTRY_FOREGROUND
)

def add_student(tree, cedula, nombre, new_window):
    tree.insert("", "end", values=(cedula, nombre))
    print(f"Nuevo estudiante agregado con cédula: {cedula} y nombre: {nombre}")
    new_window.destroy()

def edit_student(student_id):
    print(f"Editar estudiante con cédula {student_id}")

def delete_student(student_id):
    print(f"Borrar estudiante con cédula {student_id}")

def on_enter(e):
    e.widget['background'] = BUTTON_COLOR_HOVER

def on_leave(e):
    e.widget['background'] = BUTTON_COLOR

def on_click_action(tree, edit_button, delete_button):
    selected_item = tree.selection()
    if selected_item:
        selected_student = tree.item(selected_item, 'values')
        student_id = selected_student[0]

        edit_button.config(state="normal", command=lambda: edit_student(student_id))
        delete_button.config(state="normal", command=lambda: delete_student(student_id))

def open_new_student_form(tree):
    new_window = tk.Toplevel()
    new_window.title("Agregar Estudiante")
    new_window.geometry("300x200")
    new_window.configure(bg=BACKGROUND_COLOR)

    label_cedula = tk.Label(new_window, text="Cédula:", bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
    label_cedula.pack(pady=5)
    entry_cedula = tk.Entry(new_window, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
    entry_cedula.pack(pady=5)

    label_nombre = tk.Label(new_window, text="Nombre:", bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
    label_nombre.pack(pady=5)
    entry_nombre = tk.Entry(new_window, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
    entry_nombre.pack(pady=5)

    save_button = tk.Button(new_window, text="Guardar", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                            command=lambda: add_student(tree, entry_cedula.get(), entry_nombre.get(), new_window))
    save_button.pack(pady=10)

    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)
