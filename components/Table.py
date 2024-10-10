import tkinter as tk
from tkinter import ttk
from constants.Colors import BACKGROUND_COLOR, TITLE_COLOR, ENTRY_BACKGROUND, ENTRY_FOREGROUND, BUTTON_COLOR_NEW
from constants.Texts import (GLOBAL_TABLE_NIT, GLOBAL_TABLE_NAME, GLOBAL_LAST_NAME, GLOBAL_AGE, GLOBAL_SEX, GLOBAL_ADDRESS, GLOBAL_COURSE, GLOBAL_PHONE)

def create_student_table(window):
    style = ttk.Style()
    style.configure("Treeview", background=ENTRY_BACKGROUND, foreground=ENTRY_FOREGROUND, fieldbackground=BACKGROUND_COLOR, rowheight=25)
    style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), background=BACKGROUND_COLOR, foreground=BUTTON_COLOR_NEW)

    tree = ttk.Treeview(window, columns=("cedula", "nombre", "apellido", "edad", "sexo", "direccion", "curso", "telefono"), show="headings", height=8)
    tree.pack(pady=10)

    tree.heading("cedula", text=GLOBAL_TABLE_NIT) 
    tree.heading("nombre", text=GLOBAL_TABLE_NAME) 
    tree.heading("apellido", text=GLOBAL_LAST_NAME)  
    tree.heading("edad", text=GLOBAL_AGE) 
    tree.heading("sexo", text=GLOBAL_SEX)
    tree.heading("direccion", text=GLOBAL_ADDRESS)
    tree.heading("curso", text=GLOBAL_COURSE)
    tree.heading("telefono", text=GLOBAL_PHONE)

    tree.column("cedula", width=100)
    tree.column("nombre", width=100)
    tree.column("apellido", width=100)
    tree.column("edad", width=50)
    tree.column("sexo", width=50)
    tree.column("direccion", width=150)
    tree.column("curso", width=100)
    tree.column("telefono", width=100)

    return tree

def populate_table(tree):
    students = [
        {"cedula": "12345678", "nombre": "Juan", "apellido": "Pérez", "edad": "20", "sexo": "M", "direccion": "Calle 123", "curso": "3", "telefono": "555-1234"},
        {"cedula": "87654321", "nombre": "María", "apellido": "Gómez", "edad": "22", "sexo": "F", "direccion": "Avenida 456", "curso": "4", "telefono": "555-5678"},
        {"cedula": "11223344", "nombre": "Carlos", "apellido": "Díaz", "edad": "19", "sexo": "M", "direccion": "Plaza 789", "curso": "2", "telefono": "555-9012"},
    ]

    for student in students:
        tree.insert("", "end", values=(student["cedula"], student["nombre"], student["apellido"], student["edad"], student["sexo"], student["direccion"], student["curso"], student["telefono"]))

def handle_row_selection(event, tree, edit_button, delete_button, details_button, on_click_action):
    selected_item = tree.selection()
    if selected_item:
        on_click_action(tree, edit_button, delete_button, details_button)

def bind_row_selection(tree, edit_button, delete_button, details_button, on_click_action):
    tree.bind("<<TreeviewSelect>>", lambda event: handle_row_selection(event, tree, edit_button, delete_button, details_button, on_click_action))
    
    