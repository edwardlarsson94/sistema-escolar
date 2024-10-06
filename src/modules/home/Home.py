import tkinter as tk
from tkinter import ttk
from constants.Colors import (
    BACKGROUND_COLOR, TITLE_COLOR, 
    ENTRY_BACKGROUND, ENTRY_FOREGROUND
)

def edit_student(student_id):
    print(f"Editar estudiante con cédula {student_id}")

def delete_student(student_id):
    print(f"Borrar estudiante con cédula {student_id}")

def on_click_action(tree, action_type):
    selected_item = tree.selection()
    if selected_item:
        selected_student = tree.item(selected_item, 'values')
        student_id = selected_student[0]
        
        if action_type == "editar":
            edit_student(student_id)
        elif action_type == "borrar":
            delete_student(student_id)

def show_home_view():
    home_window = tk.Tk()
    home_window.title("Home")
    home_window.geometry("600x400")
    home_window.configure(bg=BACKGROUND_COLOR)

    label_title = tk.Label(home_window, text="Welcome to the Home Page!", bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=("Helvetica", 24, "bold"))
    label_title.pack(pady=20)

    style = ttk.Style()
    style.configure("Treeview", background=ENTRY_BACKGROUND, foreground=ENTRY_FOREGROUND, fieldbackground=BACKGROUND_COLOR, rowheight=25)
    style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), background=BACKGROUND_COLOR, foreground=TITLE_COLOR)

    tree = ttk.Treeview(home_window, columns=("cedula", "nombre", "acciones"), show="headings", height=8)
    tree.pack(pady=10)

    tree.heading("cedula", text="Cédula")
    tree.heading("nombre", text="Nombre y Apellido")
    tree.heading("acciones", text="Acciones")

    tree.column("cedula", width=150)
    tree.column("nombre", width=200)
    tree.column("acciones", width=200)

    students = [
        {"cedula": "12345678", "nombre": "Juan Pérez"},
        {"cedula": "87654321", "nombre": "María Gómez"},
        {"cedula": "11223344", "nombre": "Carlos Díaz"},
    ]

    for student in students:
        tree.insert("", "end", values=(student["cedula"], student["nombre"], "Editar | Borrar"))

    def on_double_click(event):
        selected_item = tree.selection()
        column = tree.identify_column(event.x)

        if column == '#3':
            clicked_action = tree.identify_region(event.x, event.y)
            if clicked_action == 'cell':
                x_pos = event.x
                if x_pos < 100:
                    on_click_action(tree, "editar")
                else:
                    on_click_action(tree, "borrar")

    tree.bind("<Double-1>", on_double_click)

    home_window.mainloop()
