import tkinter as tk
from tkinter import ttk
from api.controllers.studentController import get_all_students
from constants.Colors import BACKGROUND_COLOR, TITLE_COLOR, ENTRY_BACKGROUND, ENTRY_FOREGROUND, BUTTON_COLOR_NEW
from constants.Texts import (GLOBAL_TABLE_NIT, GLOBAL_TABLE_NAME, GLOBAL_ASIGNATURE, GLOBAL_PHONE, GLOBAL_LAST_NAME)

def create_student_table(window):
    style = ttk.Style()
    style.configure("Treeview", background=ENTRY_BACKGROUND, foreground=ENTRY_FOREGROUND, fieldbackground=BACKGROUND_COLOR, rowheight=25)
    style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), background=BACKGROUND_COLOR, foreground=BUTTON_COLOR_NEW)

    columns = ("student_id", "cedula", "nombres", "apellidos")
    tree = ttk.Treeview(window, columns=columns, show="headings", height=8)
    tree.pack(pady=10)

    tree.column("student_id", width=0, stretch=tk.NO)

    column_headings = [
        (GLOBAL_TABLE_NIT, "cedula"),
        (GLOBAL_TABLE_NAME, "nombres"),
        (GLOBAL_LAST_NAME, "apellidos")
    ]

    for text, column in column_headings:
        tree.heading(column, text=text)
        tree.column(column, width=100)

    return tree

def populate_table(tree):
    for item in tree.get_children():
        tree.delete(item)
    success, students = get_all_students()
    if success:
        for student in students:
            tree.insert("", "end", values=(
                student['student_id'],
                student['id_number'],
                student['first_name'],
                student['last_name'],
            ))
    else:
        print("No se pudo obtener la información de los estudiantes.")

# Crear tabla de docentes
def create_teacher_table(window):
    style = ttk.Style()
    style.configure("Treeview", background=ENTRY_BACKGROUND, foreground=ENTRY_FOREGROUND, fieldbackground=BACKGROUND_COLOR, rowheight=25)
    style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), background=BACKGROUND_COLOR, foreground=BUTTON_COLOR_NEW)

    # Definir solo las columnas necesarias (reemplazando fecha y asistencia por asignatura y teléfono)
    columns = ("cedula", "nombres", "asignatura", "telefono")
    tree = ttk.Treeview(window, columns=columns, show="headings", height=8)
    tree.pack(pady=10)

    # Definir encabezados para las columnas
    column_headings = [
        (GLOBAL_TABLE_NIT, "cedula"),
        (GLOBAL_TABLE_NAME, "nombres"),
        (GLOBAL_ASIGNATURE, "asignatura"),
        (GLOBAL_PHONE, "telefono")
    ]

    for text, column in column_headings:
        tree.heading(column, text=text)
        tree.column(column, width=120)

    return tree

# Poblar la tabla de docentes
def populate_teacher_table(tree):
    teachers = [
        {
            "cedula": "001", "nombres": "Carlos", "asignatura": "Matemáticas", "telefono": "555-6789",
        },
        {
            "cedula": "002", "nombres": "Laura", "asignatura": "Historia", "telefono": "555-9876",
        },
    ]

    # Insertar los datos de los docentes en la tabla
    for teacher in teachers:
        tree.insert("", "end", values=(teacher["cedula"], teacher["nombres"], teacher["asignatura"], teacher["telefono"]))

def handle_row_selection(event, tree, edit_button, delete_button, details_button, pdf_button, reports_button, on_click_action):
    selected_item = tree.selection()
    if selected_item:
        on_click_action(tree, edit_button, delete_button, details_button, pdf_button, reports_button)

def bind_row_selection(tree, edit_button, delete_button, details_button, pdf_button, reports_button, on_click_action):
    tree.bind("<<TreeviewSelect>>", lambda event: handle_row_selection(event, tree, edit_button, delete_button, details_button, pdf_button, reports_button, on_click_action))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Teacher Table")

    teacher_table = create_teacher_table(root)
    populate_teacher_table(teacher_table)

    root.mainloop()
