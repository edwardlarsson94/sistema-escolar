import tkinter as tk
from constants.Colors import (BACKGROUND_COLOR, TITLE_COLOR, BUTTON_COLOR, BUTTON_TEXT_COLOR, BUTTON_COLOR_HOVER, ENTRY_BACKGROUND, ENTRY_FOREGROUND)
from constants.Texts import (STUDENT_TITLE_EDIT, GLOBAL_STUDENT_TITLE_ADD, GLOBAL_CONFIRM_DELETE, GLOBAL_TABLE_NIT, GLOBAL_TABLE_NAME, GLOBAL_BUTTON_SAVE, GLOBAL_BUTTON_CONFIRM, GLOBAL_BUTTON_CANCEL, GLOBAL_LAST_NAME, GLOBAL_AGE, GLOBAL_SEX, GLOBAL_ADDRESS, GLOBAL_COURSE, GLOBAL_PHONE)

def add_student(tree, nit, name, lastName, age, sex, address, course, phone, new_window):
    tree.insert("", "end", values=(nit, name, lastName, age, sex, address, course, phone))
    print(f"Nuevo estudiante agregado con cédula: {nit}, nombre: {name}, apellido: {lastName}")
    new_window.destroy()

def update_student(tree, selected_item, nit, name, lastName, age, sex, address, course, phone, new_window):
    tree.item(selected_item, values=(nit, name, lastName, age, sex, address, course, phone))
    print(f"Estudiante actualizado con cédula: {nit}, nombre: {name}, apellido: {lastName}")
    new_window.destroy()

def open_student_details(student_data):
    details_window = tk.Toplevel()
    details_window.title("Detalles del Estudiante")
    details_window.geometry("300x400")
    details_window.configure(bg=BACKGROUND_COLOR)

    fields = [
        (GLOBAL_TABLE_NIT, student_data[0] if len(student_data) > 0 else "N/A"),
        (GLOBAL_TABLE_NAME, student_data[1] if len(student_data) > 1 else "N/A"),
        (GLOBAL_LAST_NAME, student_data[2] if len(student_data) > 2 else "N/A"),
        (GLOBAL_AGE, student_data[3] if len(student_data) > 3 else "N/A"),
        (GLOBAL_SEX, student_data[4] if len(student_data) > 4 else "N/A"),
        (GLOBAL_ADDRESS, student_data[5] if len(student_data) > 5 else "N/A"),
        (GLOBAL_COURSE, student_data[6] if len(student_data) > 6 else "N/A"),
        (GLOBAL_PHONE, student_data[7] if len(student_data) > 7 else "N/A")
    ]

    for label_text, value in fields:
        label = tk.Label(details_window, text=f"{label_text}: {value}", bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=("Helvetica", 12))
        label.pack(pady=5)

    close_button = tk.Button(details_window, text="Cerrar", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, command=details_window.destroy)
    close_button.pack(pady=10)
    close_button.bind("<Enter>", on_enter)
    close_button.bind("<Leave>", on_leave)

def open_edit_student_form(tree, selected_item, student_data):
    new_window = tk.Toplevel()
    new_window.title(STUDENT_TITLE_EDIT)
    new_window.geometry("400x500")
    new_window.configure(bg=BACKGROUND_COLOR)

    fields = [
        ("Cédula", GLOBAL_TABLE_NIT),
        ("Nombre", GLOBAL_TABLE_NAME),
        ("Apellido", GLOBAL_LAST_NAME),
        ("Edad", GLOBAL_AGE),
        ("Sexo", GLOBAL_SEX),
        ("Dirección", GLOBAL_ADDRESS),
        ("Año que cursa", GLOBAL_COURSE),
        ("Teléfono", GLOBAL_PHONE)
    ]

    entries = {}

    for i, (field, label_text) in enumerate(fields):
        label = tk.Label(new_window, text=label_text, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
        label.pack(pady=5)
        entry = tk.Entry(new_window, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
        entry.insert(0, student_data[i] if i < len(student_data) else "")
        entry.pack(pady=5)
        entries[field] = entry

    save_button = tk.Button(new_window, text=GLOBAL_BUTTON_SAVE, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                            command=lambda: update_student(tree, selected_item, 
                                                           entries[GLOBAL_TABLE_NIT].get(),
                                                           entries[GLOBAL_TABLE_NAME].get(),
                                                           entries[GLOBAL_LAST_NAME].get(),
                                                           entries[GLOBAL_AGE].get(),
                                                           entries[GLOBAL_SEX].get(),
                                                           entries[GLOBAL_ADDRESS].get(),
                                                           entries[GLOBAL_COURSE].get(),
                                                           entries[GLOBAL_PHONE].get(),
                                                           new_window))
    save_button.pack(pady=10)

    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)

def confirm_delete_student(tree, selected_item, student_id):
    new_window = tk.Toplevel()
    new_window.title(GLOBAL_CONFIRM_DELETE)
    new_window.geometry("300x150")
    new_window.configure(bg=BACKGROUND_COLOR)

    label_message = tk.Label(new_window, text=f"¿Estás seguro de que deseas borrar al estudiante con cédula {student_id}?", 
                             bg=BACKGROUND_COLOR, fg=TITLE_COLOR, wraplength=250)
    label_message.pack(pady=10)

    def delete_confirmed():
        tree.delete(selected_item)
        print(f"Estudiante con cédula {student_id} borrado")
        new_window.destroy()

    button_confirm = tk.Button(new_window, text=GLOBAL_BUTTON_CONFIRM, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, 
                               command=delete_confirmed)
    button_cancel = tk.Button(new_window, text=GLOBAL_BUTTON_CANCEL, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, 
                              command=new_window.destroy)

    button_confirm.bind("<Enter>", on_enter)
    button_confirm.bind("<Leave>", on_leave)
    button_cancel.bind("<Enter>", on_enter)
    button_cancel.bind("<Leave>", on_leave)

    button_confirm.pack(side="left", padx=20, pady=20)
    button_cancel.pack(side="right", padx=20, pady=20)

def on_enter(e):
    e.widget['background'] = BUTTON_COLOR_HOVER

def on_leave(e):
    e.widget['background'] = BUTTON_COLOR

def on_click_action(tree, edit_button, delete_button, details_button):
    selected_item = tree.selection()
    if selected_item:
        selected_student = tree.item(selected_item, 'values')
        edit_button.config(state="normal", command=lambda: open_edit_student_form(tree, selected_item, selected_student))
        delete_button.config(state="normal", command=lambda: confirm_delete_student(tree, selected_item, selected_student[0]))
        details_button.config(state="normal", command=lambda: open_student_details(selected_student))
    else:
        edit_button.config(state="disabled")
        delete_button.config(state="disabled")
        details_button.config(state="disabled")

def open_new_student_form(tree):
    new_window = tk.Toplevel()
    new_window.title(GLOBAL_STUDENT_TITLE_ADD)
    new_window.geometry("400x500")
    new_window.configure(bg=BACKGROUND_COLOR)

    fields = [
        ("Cédula", GLOBAL_TABLE_NIT),
        ("Nombre", GLOBAL_TABLE_NAME),
        ("Apellido", GLOBAL_LAST_NAME),
        ("Edad", GLOBAL_AGE),
        ("Sexo", GLOBAL_SEX),
        ("Dirección", GLOBAL_ADDRESS),
        ("Año que cursa", GLOBAL_COURSE),
        ("Teléfono", GLOBAL_PHONE)
    ]

    entries = {}

    for field, label_text in fields:
        label = tk.Label(new_window, text=label_text, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
        label.pack(pady=5)
        entry = tk.Entry(new_window, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
        entry.pack(pady=5)
        entries[field] = entry

    save_button = tk.Button(new_window, text=GLOBAL_BUTTON_SAVE, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                            command=lambda: add_student(tree, 
                                                        entries[GLOBAL_TABLE_NIT].get(),
                                                        entries[GLOBAL_TABLE_NAME].get(),
                                                        entries[GLOBAL_LAST_NAME].get(),
                                                        entries[GLOBAL_AGE].get(),
                                                        entries[GLOBAL_SEX].get(),
                                                        entries[GLOBAL_ADDRESS].get(),
                                                        entries[GLOBAL_COURSE].get(),
                                                        entries[GLOBAL_PHONE].get(),
                                                        new_window))
    save_button.pack(pady=10)

    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)