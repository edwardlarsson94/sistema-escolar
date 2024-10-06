import tkinter as tk
from tkinter import ttk
from constants.Colors import (
    BACKGROUND_COLOR, TITLE_COLOR, 
    ENTRY_BACKGROUND, ENTRY_FOREGROUND, BUTTON_COLOR, BUTTON_TEXT_COLOR, BUTTON_COLOR_HOVER
)

def edit_student(student_id):
    print(f"Editar estudiante con cédula {student_id}")

def delete_student(student_id):
    print(f"Borrar estudiante con cédula {student_id}")

def add_student(tree, cedula, nombre, new_window):
    tree.insert("", "end", values=(cedula, nombre))
    print(f"Nuevo estudiante agregado con cédula: {cedula} y nombre: {nombre}")
    new_window.destroy()

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

def show_home_view():
    home_window = tk.Tk()
    home_window.title("Home")
    home_window.geometry("600x500")
    home_window.configure(bg=BACKGROUND_COLOR)

    label_title = tk.Label(home_window, text="Welcome to the Home Page!", bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=("Helvetica", 24, "bold"))
    label_title.pack(pady=20)

    style = ttk.Style()
    style.configure("Treeview", background=ENTRY_BACKGROUND, foreground=ENTRY_FOREGROUND, fieldbackground=BACKGROUND_COLOR, rowheight=25)
    style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), background=BACKGROUND_COLOR, foreground=TITLE_COLOR)

    tree = ttk.Treeview(home_window, columns=("cedula", "nombre"), show="headings", height=8)
    tree.pack(pady=10)

    tree.heading("cedula", text="Cédula")
    tree.heading("nombre", text="Nombre y Apellido")
    tree.column("cedula", width=150)
    tree.column("nombre", width=200)

    students = [
        {"cedula": "12345678", "nombre": "Juan Pérez"},
        {"cedula": "87654321", "nombre": "María Gómez"},
        {"cedula": "11223344", "nombre": "Carlos Díaz"},
    ]

    for student in students:
        tree.insert("", "end", values=(student["cedula"], student["nombre"]))

    def on_row_select(event):
        on_click_action(tree, edit_button, delete_button)

    tree.bind("<<TreeviewSelect>>", on_row_select)

    actions_frame = tk.Frame(home_window, bg=BACKGROUND_COLOR)
    actions_frame.pack(pady=20)

    new_student_button = tk.Button(actions_frame, text="Agregar Estudiante", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                                   command=lambda: open_new_student_form(tree))
    new_student_button.pack(side="left", padx=10)

    edit_button = tk.Button(actions_frame, text="Editar", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", state="disabled")
    delete_button = tk.Button(actions_frame, text="Borrar", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", state="disabled")

    edit_button.bind("<Enter>", on_enter)
    edit_button.bind("<Leave>", on_leave)
    delete_button.bind("<Enter>", on_enter)
    delete_button.bind("<Leave>", on_leave)

    edit_button.pack(side="left", padx=10)
    delete_button.pack(side="left", padx=10)

    home_window.mainloop()
