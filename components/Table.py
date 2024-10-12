import tkinter as tk
from tkinter import ttk
from constants.Colors import BACKGROUND_COLOR, TITLE_COLOR, ENTRY_BACKGROUND, ENTRY_FOREGROUND, BUTTON_COLOR_NEW
from constants.Texts import (
    GLOBAL_TABLE_NIT, GLOBAL_TABLE_NAME, GLOBAL_LAST_NAME, GLOBAL_AGE, GLOBAL_SEX, 
    GLOBAL_ADDRESS, GLOBAL_COURSE, GLOBAL_PHONE, GLOBAL_BIRTH_PLACE, GLOBAL_NATIONALITY,
    GLOBAL_PREVIOUS_SCHOOL, GLOBAL_PENDING_SUBJECT, GLOBAL_WHICH_SUBJECT,
    GLOBAL_REPEATING, GLOBAL_WHICH_SUBJECTS, GLOBAL_LIVES_WITH_PARENTS,
    GLOBAL_STUDENT_EMAIL, GLOBAL_RELIGION, GLOBAL_SUBJECT, GLOBAL_NAME_AND_SURNAME, CURRENT_DATE, GLOBAL_ATTENDANCES
)

def create_student_table(window):
    style = ttk.Style()
    style.configure("Treeview", background=ENTRY_BACKGROUND, foreground=ENTRY_FOREGROUND, fieldbackground=BACKGROUND_COLOR, rowheight=25)
    style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), background=BACKGROUND_COLOR, foreground=BUTTON_COLOR_NEW)

    columns = (
        "cedula", "nombres", "apellidos"
    )

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

def create_teacher_table(window):
    style = ttk.Style()
    style.configure("Treeview", background=ENTRY_BACKGROUND, foreground=ENTRY_FOREGROUND, fieldbackground=BACKGROUND_COLOR, rowheight=25)
    style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), background=BACKGROUND_COLOR, foreground=BUTTON_COLOR_NEW)

    # Ensure that all columns are defined here, matching the fields we want to display.
    columns = ("cedula", "nombres", "apellidos", "asignatura", "fecha_actualizada", "asistencias")

    # Define the Treeview widget with the correct columns
    tree = ttk.Treeview(window, columns=columns, show="headings", height=8)
    tree.pack(pady=10)

    # Define the column headings for the table (these need to match the columns above)
    column_headings = [
        (GLOBAL_TABLE_NIT, "cedula"),
        (GLOBAL_TABLE_NAME, "nombres"),
        (GLOBAL_LAST_NAME, "apellidos"),
        (GLOBAL_SUBJECT, "asignatura"),
        (CURRENT_DATE, "fecha_actualizada"),
        (GLOBAL_ATTENDANCES, "asistencias")
    ]

    # Set the headings and column widths for each column
    for text, column in column_headings:
        tree.heading(column, text=text)
        tree.column(column, width=120)  # Adjust column width to fit content as needed

    return tree

# Populate the teacher table with data
def populate_teacher_table(tree):
    teachers = [
        {
            "cedula": "001", "nombres": "Carlos", "apellidos": "Gómez", "asignatura": "Matemáticas", 
            "fecha_actualizada": "2024-10-01", "asistencias": "95%",
        },
        {
            "cedula": "002", "nombres": "Laura", "apellidos": "Fernández", "asignatura": "Historia", 
            "fecha_actualizada": "2024-10-02", "asistencias": "98%",
        },
    ]

    # Insert each teacher into the table with the correct number of columns
    for teacher in teachers:
        tree.insert("", "end", values=(teacher["cedula"], teacher["nombres"], teacher["apellidos"], teacher["asignatura"], teacher["fecha_actualizada"], teacher["asistencias"]))


def handle_row_selection(event, tree, edit_button, delete_button, details_button, pdf_button, on_click_action):
    selected_item = tree.selection()
    if selected_item:
        on_click_action(tree, edit_button, delete_button, details_button, pdf_button)

def bind_row_selection(tree, edit_button, delete_button, details_button, pdf_button, on_click_action):
    tree.bind("<<TreeviewSelect>>", lambda event: handle_row_selection(event, tree, edit_button, delete_button, details_button, pdf_button, on_click_action))
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Teacher Table")

    teacher_table = create_teacher_table(root)
    populate_teacher_table(teacher_table)

    root.mainloop()