import tkinter as tk
from constants.Colors import BACKGROUND_COLOR, BUTTON_COLOR, BUTTON_TEXT_COLOR, BUTTON_COLOR_HOVER, TITLE_COLOR
from constants.Texts import HOME_SUBTITLE, GLOBAL_STUDENT_TITLE_ADD, HOME_BUTTON_DELETE, HOME_BUTTON_EDIT, TEACHER_TITLE_ADD, GLOBAL_STUDENT, GLOBAL_TEACHER
from components.Table import create_student_table, populate_table, bind_row_selection
from src.modules.student.views.Student import open_new_student_form, on_click_action as on_student_click_action
from src.modules.teachers.views.Teachers import open_new_teacher_form, on_click_action as on_teacher_click_action
from components.Table import create_teacher_table, populate_teacher_table  # Importamos las funciones correctas

def create_student_tab(notebook):
    student_tab = tk.Frame(notebook, bg=BACKGROUND_COLOR)
    notebook.add(student_tab, text=GLOBAL_STUDENT)

    label_title = tk.Label(student_tab, text=HOME_SUBTITLE, bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=("Helvetica", 24, "bold"))
    label_title.pack(pady=20)

    top_frame = tk.Frame(student_tab, bg=BACKGROUND_COLOR)
    top_frame.pack(pady=10)

    new_student_button = tk.Button(top_frame, text=GLOBAL_STUDENT_TITLE_ADD, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                                   command=lambda: open_new_student_form(student_tree))
    new_student_button.pack(side="left", padx=10)

    student_tree = create_student_table(student_tab)
    populate_table(student_tree)

    actions_frame = tk.Frame(student_tab, bg=BACKGROUND_COLOR)
    actions_frame.pack(pady=20)

    edit_button = tk.Button(actions_frame, text=HOME_BUTTON_EDIT, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", state="disabled")
    details_button = tk.Button(actions_frame, text="Detalles", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", state="disabled")
    delete_button = tk.Button(actions_frame, text=HOME_BUTTON_DELETE, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", state="disabled")
    pdf_button = tk.Button(actions_frame, text="Generar Certificado", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", state="disabled")

    for button in [edit_button, details_button, delete_button, pdf_button]:
        button.bind("<Enter>", lambda e: e.widget.config(bg=BUTTON_COLOR_HOVER))
        button.bind("<Leave>", lambda e: e.widget.config(bg=BUTTON_COLOR))

    edit_button.pack(side="left", padx=10)
    details_button.pack(side="left", padx=10)
    pdf_button.pack(side="left", padx=10)
    delete_button.pack(side="left", padx=10)

    bind_row_selection(student_tree, edit_button, delete_button, details_button, pdf_button, on_student_click_action)

    return student_tab

def create_teacher_tab(notebook):
    teacher_tab = tk.Frame(notebook, bg=BACKGROUND_COLOR)
    notebook.add(teacher_tab, text=GLOBAL_TEACHER)

    label_title = tk.Label(teacher_tab, text=HOME_SUBTITLE, bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=("Helvetica", 24, "bold"))
    label_title.pack(pady=20)

    top_frame = tk.Frame(teacher_tab, bg=BACKGROUND_COLOR)
    top_frame.pack(pady=10)

    new_teacher_button = tk.Button(top_frame, text=TEACHER_TITLE_ADD, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                                   command=lambda: open_new_teacher_form(teacher_tree))
    new_teacher_button.pack(side="left", padx=10)

    # Cambiamos a `create_teacher_table` para que cree la tabla de profesores
    teacher_tree = create_teacher_table(teacher_tab)
    populate_teacher_table(teacher_tree)

    actions_frame = tk.Frame(teacher_tab, bg=BACKGROUND_COLOR)
    actions_frame.pack(pady=20)

    edit_button = tk.Button(actions_frame, text=HOME_BUTTON_EDIT, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", state="disabled")
    details_button = tk.Button(actions_frame, text="Detalles", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", state="disabled")
    delete_button = tk.Button(actions_frame, text=HOME_BUTTON_DELETE, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", state="disabled")
    attendance_button = tk.Button(actions_frame, text="Asistencia", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", state="disabled")

    for button in [edit_button, details_button, delete_button, attendance_button]:
        button.bind("<Enter>", lambda e: e.widget.config(bg=BUTTON_COLOR_HOVER))
        button.bind("<Leave>", lambda e: e.widget.config(bg=BUTTON_COLOR))

    edit_button.pack(side="left", padx=10)
    details_button.pack(side="left", padx=10)
    delete_button.pack(side="left", padx=10)
    attendance_button.pack(side="left", padx=10)

    bind_row_selection(teacher_tree, edit_button, delete_button, details_button, attendance_button, on_teacher_click_action)

    return teacher_tab
