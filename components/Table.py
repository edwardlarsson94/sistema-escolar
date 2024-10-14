import tkinter as tk
from tkinter import ttk
from api.controllers.studentController import get_all_students
from api.controllers.teacherController import get_all_teachers
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

def create_teacher_table(window):
    style = ttk.Style()
    style.configure("Treeview", background=ENTRY_BACKGROUND, foreground=ENTRY_FOREGROUND, fieldbackground=BACKGROUND_COLOR, rowheight=25)
    style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), background=BACKGROUND_COLOR, foreground=BUTTON_COLOR_NEW)

    columns = ("teacher_id", "cedula", "nombres", "asignatura", "telefono")
    tree = ttk.Treeview(window, columns=columns, show="headings", height=8)
    tree.pack(pady=10)

    tree.column("teacher_id", width=0, stretch=tk.NO)

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

def populate_teacher_table(tree):
    for item in tree.get_children():
        tree.delete(item)
    success, teachers = get_all_teachers()
    if success:
        for teacher in teachers:
            tree.insert("", "end", values=(
                teacher["teacher_id"],  # Este es el ID oculto
                teacher["id_number"],
                teacher["first_name"],
                teacher["subject"],
                teacher["phone"]
            ))
    else:
        print("No se pudo obtener la información de los profesores.")
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
