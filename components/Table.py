import tkinter as tk
from tkinter import ttk
from constants.Colors import BACKGROUND_COLOR, TITLE_COLOR, ENTRY_BACKGROUND, ENTRY_FOREGROUND
from constants.Texts import (GLOBAL_TABLE_NIT, GLOBAL_NAME_AND_SURNAME)


def create_student_table(window):
    style = ttk.Style()
    style.configure("Treeview", background=ENTRY_BACKGROUND, foreground=ENTRY_FOREGROUND, fieldbackground=BACKGROUND_COLOR, rowheight=25)
    style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), background=BACKGROUND_COLOR, foreground=TITLE_COLOR)

    tree = ttk.Treeview(window, columns=("cedula", "nombre"), show="headings", height=8)
    tree.pack(pady=10)

    tree.heading("cedula", text=GLOBAL_TABLE_NIT)
    tree.heading("nombre", text=GLOBAL_NAME_AND_SURNAME)
    tree.column("cedula", width=150)
    tree.column("nombre", width=200)

    return tree

def populate_table(tree):
    students = [
        {"cedula": "12345678", "nombre": "Juan Pérez"},
        {"cedula": "87654321", "nombre": "María Gómez"},
        {"cedula": "11223344", "nombre": "Carlos Díaz"},
    ]

    for student in students:
        tree.insert("", "end", values=(student["cedula"], student["nombre"]))

def handle_row_selection(event, tree, edit_button, delete_button, on_click_action):
    selected_item = tree.selection()
    if selected_item:
        on_click_action(tree, edit_button, delete_button)

def bind_row_selection(tree, edit_button, delete_button, on_click_action):
    tree.bind("<<TreeviewSelect>>", lambda event: handle_row_selection(event, tree, edit_button, delete_button, on_click_action))
