import tkinter as tk
from constants.Colors import (BACKGROUND_COLOR, TITLE_COLOR, BUTTON_COLOR, BUTTON_TEXT_COLOR, BUTTON_COLOR_HOVER, ENTRY_BACKGROUND, ENTRY_FOREGROUND)
from constants.Texts import (STUDENT_TITLE_EDIT,GLOBAL_TABLE_NIT, GLOBAL_TABLE_NAME, GLOBAL_BUTTON_SAVE, GLOBAL_TABLE_NIT,GLOBAL_BUTTON_CONFIRM,GLOBAL_BUTTON_CANCEL)

def add_teacher(tree, nit, name, new_window):
    tree.insert("", "end", values=(nit, name))
    print(f"Nuevo docente agregado con cédula: {nit} y nombre: {name}")
    new_window.destroy()

def update_teacher(tree, selected_item, nit, name, new_window):
    tree.item(selected_item, values=(nit, name))
    print(f"Docente actualizado con cédula: {nit} y nombre: {name}")
    new_window.destroy()

def open_edit_teacher_form(tree, selected_item, teacher_data):
    new_window = tk.Toplevel()
    new_window.title(GLOBAL_TABLE_NIT)
    new_window.geometry("300x200")
    new_window.configure(bg=BACKGROUND_COLOR)

    label_nit = tk.Label(new_window, text=GLOBAL_TABLE_NIT, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
    label_nit.pack(pady=5)
    entry_nit = tk.Entry(new_window, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
    entry_nit.insert(0, teacher_data[0])
    entry_nit.pack(pady=5)

    label_name = tk.Label(new_window, text=GLOBAL_TABLE_NAME, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
    label_name.pack(pady=5)
    entry_name = tk.Entry(new_window, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
    entry_name.insert(0, teacher_data[1])
    entry_name.pack(pady=5)

    save_button = tk.Button(new_window, text=GLOBAL_BUTTON_SAVE, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                            command=lambda: update_teacher(tree, selected_item, entry_nit.get(), entry_name.get(), new_window))
    save_button.pack(pady=10)

    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)

def confirm_delete_teacher(tree, selected_item, teacher_id):
    new_window = tk.Toplevel()
    new_window.title("Confirmar Borrado")
    new_window.geometry("300x150")
    new_window.configure(bg=BACKGROUND_COLOR)

    label_message = tk.Label(new_window, text=f"¿Estás seguro de que deseas borrar al docente con cédula {teacher_id}?", 
                             bg=BACKGROUND_COLOR, fg=TITLE_COLOR, wraplength=250)
    label_message.pack(pady=10)

    def delete_confirmed():
        tree.delete(selected_item)
        print(f"Docente con cédula {teacher_id} borrado")
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

def on_click_action(tree, edit_button, delete_button):
    selected_item = tree.selection()
    if selected_item:
        selected_teacher = tree.item(selected_item, 'values')
        teacher_id = selected_teacher[0]

        edit_button.config(state="normal", command=lambda: open_edit_teacher_form(tree, selected_item, selected_teacher))
        delete_button.config(state="normal", command=lambda: confirm_delete_teacher(tree, selected_item, teacher_id))

def open_new_teacher_form(tree):
    new_window = tk.Toplevel()
    new_window.title("Agregar Docente")
    new_window.geometry("300x200")
    new_window.configure(bg=BACKGROUND_COLOR)

    label_nit = tk.Label(new_window, text=GLOBAL_TABLE_NIT, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
    label_nit.pack(pady=5)
    entry_nit = tk.Entry(new_window, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
    entry_nit.pack(pady=5)

    label_name = tk.Label(new_window, text=GLOBAL_TABLE_NAME, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
    label_name.pack(pady=5)
    entry_name = tk.Entry(new_window, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
    entry_name.pack(pady=5)

    save_button = tk.Button(new_window, text=GLOBAL_BUTTON_SAVE, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                            command=lambda: add_teacher(tree, entry_nit.get(), entry_name.get(), new_window))
    save_button.pack(pady=10)

    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)
    
    