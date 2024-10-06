import tkinter as tk
from tkinter import ttk
from constants.Colors import (
    BACKGROUND_COLOR, TITLE_COLOR, LABEL_COLOR, BUTTON_COLOR, BUTTON_COLOR_HOVER, BUTTON_TEXT_COLOR, 
    ENTRY_BACKGROUND, ENTRY_FOREGROUND
)

def edit_student(student_id):
    print(f"Editar estudiante con cédula {student_id}")

def delete_student(student_id):
    print(f"Borrar estudiante con cédula {student_id}")

def on_enter(e):
    e.widget['background'] = BUTTON_COLOR_HOVER

def on_leave(e):
    e.widget['background'] = BUTTON_COLOR

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
    tree.heading("nombre", text="Nombre")
    tree.heading("acciones", text="Acciones")

    tree.column("cedula", width=150)
    tree.column("nombre", width=200)
    tree.column("acciones", width=150)

    students = [
        {"cedula": "12345678", "nombre": "Juan Pérez"},
        {"cedula": "87654321", "nombre": "María Gómez"},
        {"cedula": "11223344", "nombre": "Carlos Díaz"},
    ]

    for student in students:
        student_id = student["cedula"]

        actions_frame = tk.Frame(home_window, bg=BACKGROUND_COLOR)
        edit_button = tk.Button(actions_frame, text="Editar", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                                command=lambda sid=student_id: edit_student(sid))
        delete_button = tk.Button(actions_frame, text="Borrar", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                                  command=lambda sid=student_id: delete_student(sid))

        edit_button.bind("<Enter>", on_enter)
        edit_button.bind("<Leave>", on_leave)
        delete_button.bind("<Enter>", on_enter)
        delete_button.bind("<Leave>", on_leave)

        edit_button.pack(side="left", padx=5)
        delete_button.pack(side="left", padx=5)

        tree.insert("", "end", values=(student["cedula"], student["nombre"], actions_frame))

    home_window.mainloop()
