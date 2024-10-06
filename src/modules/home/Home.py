import tkinter as tk
from constants.Colors import (
    BACKGROUND_COLOR, TITLE_COLOR, 
    BUTTON_COLOR, BUTTON_TEXT_COLOR, BUTTON_COLOR_HOVER
)
from components.Table import create_student_table, populate_table, bind_row_selection
from src.modules.student.Student import open_new_student_form, on_click_action, edit_student, delete_student

def show_home_view():
    home_window = tk.Tk()
    home_window.title("Home")
    home_window.geometry("600x500")
    home_window.configure(bg=BACKGROUND_COLOR)

    label_title = tk.Label(home_window, text="Welcome to the Home Page!", bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=("Helvetica", 24, "bold"))
    label_title.pack(pady=20)

    top_frame = tk.Frame(home_window, bg=BACKGROUND_COLOR)
    top_frame.pack(pady=10)

    new_student_button = tk.Button(top_frame, text="Agregar Estudiante", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                                   command=lambda: open_new_student_form(tree))
    new_student_button.pack(side="left", padx=10)

    tree = create_student_table(home_window)
    populate_table(tree)

    actions_frame = tk.Frame(home_window, bg=BACKGROUND_COLOR)
    actions_frame.pack(pady=20)

    edit_button = tk.Button(actions_frame, text="Editar", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", state="disabled")
    delete_button = tk.Button(actions_frame, text="Borrar", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", state="disabled")

    edit_button.bind("<Enter>", lambda e: e.widget.config(bg=BUTTON_COLOR_HOVER))
    edit_button.bind("<Leave>", lambda e: e.widget.config(bg=BUTTON_COLOR))
    delete_button.bind("<Enter>", lambda e: e.widget.config(bg=BUTTON_COLOR_HOVER))
    delete_button.bind("<Leave>", lambda e: e.widget.config(bg=BUTTON_COLOR))

    edit_button.pack(side="left", padx=10)
    delete_button.pack(side="left", padx=10)
    bind_row_selection(tree, edit_button, delete_button, on_click_action)

    home_window.mainloop()
