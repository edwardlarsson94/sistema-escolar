import tkinter as tk
from tkinter import ttk
from constants.Colors import BACKGROUND_COLOR, TITLE_COLOR, ENTRY_BACKGROUND, ENTRY_FOREGROUND, BUTTON_COLOR_NEW
from constants.Texts import (
    GLOBAL_TABLE_NIT, GLOBAL_TABLE_NAME, GLOBAL_LAST_NAME, GLOBAL_AGE, GLOBAL_SEX, 
    GLOBAL_ADDRESS, GLOBAL_COURSE, GLOBAL_PHONE, GLOBAL_BIRTH_PLACE, GLOBAL_NATIONALITY,
    GLOBAL_PREVIOUS_SCHOOL, GLOBAL_PENDING_SUBJECT, GLOBAL_WHICH_SUBJECT,
    GLOBAL_REPEATING, GLOBAL_WHICH_SUBJECTS, GLOBAL_LIVES_WITH_PARENTS,
    GLOBAL_STUDENT_EMAIL, GLOBAL_RELIGION
)

def create_student_table(window):
    style = ttk.Style()
    style.configure("Treeview", background=ENTRY_BACKGROUND, foreground=ENTRY_FOREGROUND, fieldbackground=BACKGROUND_COLOR, rowheight=25)
    style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), background=BACKGROUND_COLOR, foreground=BUTTON_COLOR_NEW)

    columns = (
        "cedula", "nombres", "apellidos", "telefono"
    )

    tree = ttk.Treeview(window, columns=columns, show="headings", height=8)
    tree.pack(pady=10)

    column_headings = [
        (GLOBAL_TABLE_NIT, "cedula"),
        (GLOBAL_TABLE_NAME, "nombres"),
        (GLOBAL_LAST_NAME, "apellidos"),
        (GLOBAL_PHONE, "telefono")
    ]

    for text, column in column_headings:
        tree.heading(column, text=text)
        tree.column(column, width=100)

    return tree

def populate_table(tree):
    students = [
        {
            "cedula": "12345678", "nombres": "Juan", "apellidos": "Pérez",
             "telefono": "555-1234"
        },
        # Puedes agregar más estudiantes aquí siguiendo el mismo formato
    ]

    for student in students:
        tree.insert("", "end", values=tuple(student.values()))

def handle_row_selection(event, tree, edit_button, delete_button, details_button, on_click_action):
    selected_item = tree.selection()
    if selected_item:
        on_click_action(tree, edit_button, delete_button, details_button)

def bind_row_selection(tree, edit_button, delete_button, details_button, on_click_action):
    tree.bind("<<TreeviewSelect>>", lambda event: handle_row_selection(event, tree, edit_button, delete_button, details_button, on_click_action))