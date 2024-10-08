import tkinter as tk
from tkinter import ttk
from constants.Colors import (BACKGROUND_COLOR, TITLE_COLOR, BUTTON_COLOR, BUTTON_TEXT_COLOR, BUTTON_COLOR_HOVER)
from constants.Texts import (HOME_SUBTITLE, GLOBAL_STUDENT_TITLE_ADD, HOME_BUTTON_DELETE, HOME_BUTTON_EDIT, PROFESSOR_TITLE_ADD, GLOBAL_BUTTON_SAVE)

from components.Table import create_student_table, populate_table, bind_row_selection
from src.modules.student.Student import open_new_student_form, on_click_action
from src.modules.teachers.Teachers import open_new_teacher_form, on_click_action as on_professor_click_action

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
                                   command=lambda: open_new_student_form(student_tree))
    new_student_button.pack(side="left", padx=10)

    student_tree = create_student_table(student_tab)
    populate_table(student_tree)

    student_actions_frame = tk.Frame(student_tab, bg=BACKGROUND_COLOR)
    student_actions_frame.pack(pady=20)

    edit_student_button = tk.Button(student_actions_frame, text=HOME_BUTTON_EDIT, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", state="disabled", command=lambda: open_edit_student_form(student_tree, None, None))
    delete_student_button = tk.Button(student_actions_frame, text=HOME_BUTTON_DELETE, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", state="disabled")

    edit_student_button.bind("<Enter>", lambda e: e.widget.config(bg=BUTTON_COLOR_HOVER))
    edit_student_button.bind("<Leave>", lambda e: e.widget.config(bg=BUTTON_COLOR))
    delete_student_button.bind("<Enter>", lambda e: e.widget.config(bg=BUTTON_COLOR_HOVER))
    delete_student_button.bind("<Leave>", lambda e: e.widget.config(bg=BUTTON_COLOR))

    edit_student_button.pack(side="left", padx=10)
    delete_student_button.pack(side="left", padx=10)
    bind_row_selection(student_tree, edit_student_button, delete_student_button, on_click_action)

    teacher_tab = tk.Frame(notebook, bg=BACKGROUND_COLOR)
    notebook.add(teacher_tab, text="Profesores")

    teacher_label = tk.Label(teacher_tab, text="Profesores", bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=("Helvetica", 24, "bold"))
    teacher_label.pack(pady=20)

    top_teacher_frame = tk.Frame(teacher_tab, bg=BACKGROUND_COLOR)
    top_teacher_frame.pack(pady=10)

    new_teacher_button = tk.Button(top_teacher_frame, text=PROFESSOR_TITLE_ADD, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                                   command=lambda: open_new_teacher_form(teacher_tree))
    new_teacher_button.pack(side="left", padx=10)

    teacher_tree = create_student_table(teacher_tab)  # Puedes cambiar esta función si necesitas una estructura diferente
    populate_table(teacher_tree)

    teacher_actions_frame = tk.Frame(teacher_tab, bg=BACKGROUND_COLOR)
    teacher_actions_frame.pack(pady=20)

    edit_teacher_button = tk.Button(teacher_actions_frame, text=HOME_BUTTON_EDIT, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", state="disabled", command=lambda: open_edit_teacher_form(teacher_tree, None, None))
    delete_teacher_button = tk.Button(teacher_actions_frame, text=HOME_BUTTON_DELETE, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", state="disabled")

    edit_teacher_button.bind("<Enter>", lambda e: e.widget.config(bg=BUTTON_COLOR_HOVER))
    edit_teacher_button.bind("<Leave>", lambda e: e.widget.config(bg=BUTTON_COLOR))
    delete_teacher_button.bind("<Enter>", lambda e: e.widget.config(bg=BUTTON_COLOR_HOVER))
    delete_teacher_button.bind("<Leave>", lambda e: e.widget.config(bg=BUTTON_COLOR))

    edit_teacher_button.pack(side="left", padx=10)
    delete_teacher_button.pack(side="left", padx=10)
    bind_row_selection(teacher_tree, edit_teacher_button, delete_teacher_button, on_professor_click_action)

    home_window.mainloop()
