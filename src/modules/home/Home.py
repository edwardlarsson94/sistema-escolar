import tkinter as tk
from tkinter import ttk
from constants.Colors import (BACKGROUND_COLOR, TITLE_COLOR, BUTTON_COLOR, BUTTON_TEXT_COLOR, BUTTON_COLOR_HOVER)
from constants.Texts import (HOME_SUBTITLE, GLOBAL_STUDENT_TITLE_ADD, HOME_BUTTON_DELETE, HOME_BUTTON_EDIT)

from components.Table import create_student_table, populate_table, bind_row_selection
from src.modules.student.Student import open_new_student_form, on_click_action

def show_home_view():
    home_window = tk.Tk()
    home_window.title("Home")
    home_window.geometry("600x500")
    home_window.configure(bg=BACKGROUND_COLOR)

    notebook = ttk.Notebook(home_window)
    notebook.pack(expand=True, fill='both')

    student_tab = tk.Frame(notebook, bg=BACKGROUND_COLOR)
    notebook.add(student_tab, text="Estudiantes")

    label_title = tk.Label(student_tab, text=HOME_SUBTITLE, bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=("Helvetica", 24, "bold"))
    label_title.pack(pady=20)

    top_frame = tk.Frame(student_tab, bg=BACKGROUND_COLOR)
    top_frame.pack(pady=10)

    new_student_button = tk.Button(top_frame, text=GLOBAL_STUDENT_TITLE_ADD, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                                   command=lambda: open_new_student_form(tree))
    new_student_button.pack(side="left", padx=10)

    tree = create_student_table(student_tab)
    populate_table(tree)

    actions_frame = tk.Frame(student_tab, bg=BACKGROUND_COLOR)
    actions_frame.pack(pady=20)

    edit_button = tk.Button(actions_frame, text=HOME_BUTTON_EDIT, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", state="disabled", command=lambda: open_edit_student_form(tree, None, None))
    delete_button = tk.Button(actions_frame, text=HOME_BUTTON_DELETE, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", state="disabled")

    edit_button.bind("<Enter>", lambda e: e.widget.config(bg=BUTTON_COLOR_HOVER))
    edit_button.bind("<Leave>", lambda e: e.widget.config(bg=BUTTON_COLOR))
    delete_button.bind("<Enter>", lambda e: e.widget.config(bg=BUTTON_COLOR_HOVER))
    delete_button.bind("<Leave>", lambda e: e.widget.config(bg=BUTTON_COLOR))

    edit_button.pack(side="left", padx=10)
    delete_button.pack(side="left", padx=10)
    bind_row_selection(tree, edit_button, delete_button, on_click_action)

    teacher_tab = tk.Frame(notebook, bg=BACKGROUND_COLOR)
    notebook.add(teacher_tab, text="Profesores")

    teacher_label = tk.Label(teacher_tab, text="Profesores", bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=("Helvetica", 24, "bold"))
    teacher_label.pack(pady=20)

    home_window.mainloop()
