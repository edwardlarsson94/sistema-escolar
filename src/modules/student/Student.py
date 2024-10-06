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

def update_student(tree, selected_item, cedula, nombre, new_window):
    tree.item(selected_item, values=(cedula, nombre))
    print(f"Estudiante actualizado con cédula: {cedula} y nombre: {nombre}")
    new_window.destroy()

def open_edit_student_form(tree, selected_item, student_data):
    new_window = tk.Toplevel()
    new_window.title("Editar Estudiante")
    new_window.geometry("300x200")
    new_window.configure(bg=BACKGROUND_COLOR)

    label_cedula = tk.Label(new_window, text="Cédula:", bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
    label_cedula.pack(pady=5)
    entry_cedula = tk.Entry(new_window, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
    entry_cedula.insert(0, student_data[0])
    entry_cedula.pack(pady=5)

    label_nombre = tk.Label(new_window, text="Nombre:", bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
    label_nombre.pack(pady=5)
    entry_nombre = tk.Entry(new_window, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
    entry_nombre.insert(0, student_data[1])
    entry_nombre.pack(pady=5)

    save_button = tk.Button(new_window, text="Guardar", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                            command=lambda: update_student(tree, selected_item, entry_cedula.get(), entry_nombre.get(), new_window))
    save_button.pack(pady=10)

    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)

def confirm_delete_student(tree, selected_item, student_id):
    new_window = tk.Toplevel()
    new_window.title("Confirmar Borrado")
    new_window.geometry("300x150")
    new_window.configure(bg=BACKGROUND_COLOR)

    label_message = tk.Label(new_window, text=f"¿Estás seguro de que deseas borrar al estudiante con cédula {student_id}?", 
                             bg=BACKGROUND_COLOR, fg=TITLE_COLOR, wraplength=250)
    label_message.pack(pady=10)

    def delete_confirmed():
        tree.delete(selected_item)
        print(f"Estudiante con cédula {student_id} borrado")
        new_window.destroy()

    button_confirm = tk.Button(new_window, text="Confirmar", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, 
                               command=delete_confirmed)
    button_cancel = tk.Button(new_window, text="Cancelar", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, 
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
