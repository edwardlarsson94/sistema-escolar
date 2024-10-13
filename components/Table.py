import tkinter as tk
from tkinter import ttk
from constants.Colors import BACKGROUND_COLOR, TITLE_COLOR, ENTRY_BACKGROUND, ENTRY_FOREGROUND, BUTTON_COLOR_NEW
from constants.Texts import (GLOBAL_TABLE_NIT, GLOBAL_TABLE_NAME, CURRENT_DATE, GLOBAL_ATTENDANCES, GLOBAL_LAST_NAME)

# Crear tabla de estudiantes
def create_student_table(window):
    style = ttk.Style()
    style.configure("Treeview", background=ENTRY_BACKGROUND, foreground=ENTRY_FOREGROUND, fieldbackground=BACKGROUND_COLOR, rowheight=25)
    style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), background=BACKGROUND_COLOR, foreground=BUTTON_COLOR_NEW)

    columns = ("cedula", "nombres", "apellidos")
    tree = ttk.Treeview(window, columns=columns, show="headings", height=8)
    tree.pack(pady=10)

    column_headings = [
        (GLOBAL_TABLE_NIT, "cedula"),
        (GLOBAL_TABLE_NAME, "nombres"),
        (GLOBAL_LAST_NAME, "apellidos")
    ]

    for text, column in column_headings:
        tree.heading(column, text=text)
        tree.column(column, width=100)

    return tree

# Poblar la tabla de estudiantes
def populate_table(tree):
    students = [
        {
            "cedula": "12345678", "nombres": "Juan", "apellidos": "Pérez", "lugar_nacimiento": "Ciudad", 
            "nacionalidad": "Mexicana", "edad": "16", "dia_nacimiento": "10", "mes_nacimiento": "Mayo", 
            "año_nacimiento": "2005", "plantel_procedencia": "Escuela ABC", "materia_pendiente": "No", "cual": "", 
            "direccion": "Calle Falsa 123", "repite": "No", "cuales_materias": "", "vive_con_padres": "Sí", 
            "email": "juan@example.com", "religion": "Católica", "sexo": "Masculino", "año_cursa": "Segundo", "telefono": "555-1234",
        },
    ]

    for student in students:
        tree.insert("", "end", values=tuple(student.values()))

# Crear tabla de docentes
def create_teacher_table(window):
    style = ttk.Style()
    style.configure("Treeview", background=ENTRY_BACKGROUND, foreground=ENTRY_FOREGROUND, fieldbackground=BACKGROUND_COLOR, rowheight=25)
    style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), background=BACKGROUND_COLOR, foreground=BUTTON_COLOR_NEW)

    # Definir solo las columnas necesarias (sin apellidos y asignatura)
    columns = ("cedula", "nombres", "fecha_actualizada", "asistencias")
    tree = ttk.Treeview(window, columns=columns, show="headings", height=8)
    tree.pack(pady=10)

    # Definir encabezados para las columnas (sin apellidos y asignatura)
    column_headings = [
        (GLOBAL_TABLE_NIT, "cedula"),
        (GLOBAL_TABLE_NAME, "nombres"),
        (CURRENT_DATE, "fecha_actualizada"),
        (GLOBAL_ATTENDANCES, "asistencias")
    ]

    for text, column in column_headings:
        tree.heading(column, text=text)
        tree.column(column, width=120)

    return tree

# Poblar la tabla de docentes
def populate_teacher_table(tree):
    teachers = [
        {
            "cedula": "001", "nombres": "Carlos", "fecha_actualizada": "2024-10-01", "asistencias": "no",
        },
        {
            "cedula": "002", "nombres": "Laura", "fecha_actualizada": "2024-10-02", "asistencias": "no",
        },
    ]

    # Insertar los datos de los docentes en la tabla (sin apellidos ni asignatura)
    for teacher in teachers:
        tree.insert("", "end", values=(teacher["cedula"], teacher["nombres"], teacher["fecha_actualizada"], teacher["asistencias"]))

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
