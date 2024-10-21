import tkinter as tk
from tkinter import messagebox
from api.controllers.attendanceController import register_teacher_attendance
from api.controllers.teacherController import add_teacher_new, get_teacher_details, remove_teacher, update_teacher_by_id
from constants.Colors import (BACKGROUND_COLOR, TITLE_COLOR, BUTTON_COLOR, BUTTON_TEXT_COLOR, BUTTON_COLOR_HOVER, ENTRY_BACKGROUND, ENTRY_FOREGROUND)
from constants.Texts import (GLOBAL_TITLE_EDIT, TEACHER_TITLE_ADD, GLOBAL_CONFIRM_DELETE, GLOBAL_TABLE_NIT, GLOBAL_TABLE_NAME, GLOBAL_BUTTON_SAVE, GLOBAL_BUTTON_CONFIRM, GLOBAL_BUTTON_CANCEL, GLOBAL_LAST_NAME, GLOBAL_AGE, GLOBAL_SEX, GLOBAL_ADDRESS, GLOBAL_ASIGNATURE, GLOBAL_PHONE)
from components.Table import populate_teacher_table 

fields = [
    ("Cédula", GLOBAL_TABLE_NIT),
    ("Nombres", GLOBAL_TABLE_NAME),
    ("Apellido", GLOBAL_LAST_NAME),
    ("Edad", GLOBAL_AGE),
    ("Sexo", GLOBAL_SEX),
    ("Dirección", GLOBAL_ADDRESS),
    ("Asignatura", GLOBAL_ASIGNATURE),
    ("Teléfono", GLOBAL_PHONE)
]

# Actions

def add_teacher(tree, id_number, name, lastName, age, sex, address, subject, phone, new_window):
    # Validate input first
    if not validate_teacher_input(tree, id_number, name, lastName, age, sex, address, subject, phone):
        return

    success, message = add_teacher_new(id_number, name, lastName, age, sex, address, subject, phone)
    if success:
        tree.insert("", "end", values=(id_number, name, lastName, age, sex, address, subject, phone))
        print(f"Nuevo docente agregado con cédula: {id_number}, nombre: {name}, apellido: {lastName}")
        populate_teacher_table(tree)
        messagebox.showinfo("Éxito", "Docente agregado exitosamente.")
        new_window.destroy()
    else:
        messagebox.showerror("Error", message)

def update_teacher(tree, selected_item, id_number, name, lastName, age, sex, address, subject, phone, new_window):
    # Validate input first
    if not validate_teacher_input(tree, id_number, name, lastName, age, sex, address, subject, phone):
        return

    teacher_id = tree.item(selected_item, 'values')[0]
    
    success, message = update_teacher_by_id(teacher_id, id_number, name, lastName, age, sex, address, subject, phone)
    if success:
        tree.item(selected_item, values=(id_number, name, lastName, age, sex, address, subject, phone))
        print(f"Docente actualizado con cédula: {id_number}, nombre: {name}, apellido: {lastName}")
        populate_teacher_table(tree)
        messagebox.showinfo("Éxito", "Docente actualizado exitosamente.")
        new_window.destroy()
    else:
        messagebox.showerror("Error", message)

        
def validate_teacher_fields(id_number, name, lastName, age, sex, address, subject, phone):
    """
    Validates all teacher fields according to specific rules
    Returns: (bool, str) - (is_valid, error_message)
    """
    # Validate ID Number (Cédula)
    if not id_number:
        return False, "La cédula es obligatoria"
    
    # Verificar formato V-números
    if not id_number.startswith('V-'):
        return False, "La cédula debe comenzar con 'V-'"
    
    # Verificar que después del V- solo haya números
    numbers_part = id_number[2:]  # Obtener la parte después del V-
    if not numbers_part.isdigit():
        return False, "La cédula debe tener el formato V-números (ejemplo: V-12345678)"
    
    # Verificar longitud de la parte numérica
    if len(numbers_part) < 7 or len(numbers_part) > 8:
        return False, "La parte numérica de la cédula debe tener entre 7 y 8 dígitos"

    # Validate Name
    if not name:
        return False, "El nombre es obligatorio"
    if len(name) < 2:
        return False, "El nombre debe tener al menos 2 caracteres"
    if not all(char.isalpha() or char.isspace() for char in name):
        return False, "El nombre solo debe contener letras y espacios"

    # Validate Last Name
    if not lastName:
        return False, "El apellido es obligatorio"
    if len(lastName) < 2:
        return False, "El apellido debe tener al menos 2 caracteres"
    if not all(char.isalpha() or char.isspace() for char in lastName):
        return False, "El apellido solo debe contener letras y espacios"

    # Validate Age
    if not age:
        return False, "La edad es obligatoria"
    try:
        age_num = int(age)
        if age_num < 18 or age_num > 80:
            return False, "La edad debe estar entre 18 y 80 años"
    except ValueError:
        return False, "La edad debe ser un número válido"

    # Validate Sex
    valid_sex_options = ['M', 'F', 'Masculino', 'Femenino']
    if not sex:
        return False, "El sexo es obligatorio"
    if sex.upper() not in [opt.upper() for opt in valid_sex_options]:
        return False, "El sexo debe ser 'M' o 'F' (o Masculino/Femenino)"

    # Validate Address
    if not address:
        return False, "La dirección es obligatoria"
    if len(address) < 5:
        return False, "La dirección debe tener al menos 5 caracteres"
    if len(address) > 200:
        return False, "La dirección no debe exceder los 200 caracteres"

    # Validate Subject
    if not subject:
        return False, "La asignatura es obligatoria"
    if len(subject) < 2:
        return False, "La asignatura debe tener al menos 2 caracteres"
    if len(subject) > 50:
        return False, "La asignatura no debe exceder los 50 caracteres"

    # Validate Phone
    if not phone:
        return False, "El teléfono es obligatorio"
    if not phone.replace('-', '').replace('+', '').isdigit():
        return False, "El teléfono debe contener solo números, guiones o el símbolo +"
    if len(phone.replace('-', '').replace('+', '')) < 7:
        return False, "El teléfono debe tener al menos 7 dígitos"
    if len(phone.replace('-', '').replace('+', '')) > 15:
        return False, "El teléfono no debe exceder los 15 dígitos"

    return True, ""

def validate_teacher_input(tree, id_number, name, lastName, age, sex, address, subject, phone):
    """
    Validates teacher input before adding or updating
    Returns: bool - indicating if validation passed
    """
    is_valid, error_message = validate_teacher_fields(
        id_number, name, lastName, age, sex, address, subject, phone
    )
    
    if not is_valid:
        messagebox.showerror("Error de Validación", error_message)
        return False
    
    return True


# Windows

def open_new_teacher_form(tree):
    new_window = tk.Toplevel()
    new_window.title(TEACHER_TITLE_ADD)
    new_window.geometry("600x200")
    new_window.configure(bg=BACKGROUND_COLOR)

    entries = {}

    for i, (field, label_text) in enumerate(fields):
        row = i // 2
        col = i % 2

        label = tk.Label(new_window, text=label_text, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
        label.grid(row=row, column=col * 2, padx=(10, 5), pady=5, sticky='e')

        entry = tk.Entry(new_window, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
        entry.grid(row=row, column=(col * 2) + 1, padx=(0, 10), pady=5, sticky='w')
        entries[field] = entry

    save_button = tk.Button(new_window, text=GLOBAL_BUTTON_SAVE, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                            command=lambda: add_teacher(tree, 
                                                        entries[GLOBAL_TABLE_NIT].get(),
                                                        entries[GLOBAL_TABLE_NAME].get(),
                                                        entries[GLOBAL_LAST_NAME].get(),
                                                        entries[GLOBAL_AGE].get(),
                                                        entries[GLOBAL_SEX].get(),
                                                        entries[GLOBAL_ADDRESS].get(),
                                                        entries[GLOBAL_ASIGNATURE].get(),
                                                        entries[GLOBAL_PHONE].get(),
                                                        new_window))
    save_button.grid(row=(len(fields) // 1) + 1, column=1, pady=10, columnspan=3)

    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)

def open_edit_teacher_form(tree, selected_item):
    teacher_id = tree.item(selected_item, 'values')[0]

    success, teacher_data = get_teacher_details(teacher_id)
    if not success:
        messagebox.showerror("Error", teacher_data)
        return

    new_window = tk.Toplevel()
    new_window.title(GLOBAL_TITLE_EDIT)
    new_window.geometry("600x200")
    new_window.configure(bg=BACKGROUND_COLOR)

    entries = {}

    data_keys = {
        GLOBAL_TABLE_NIT: "id_number",
        GLOBAL_TABLE_NAME: "first_name",
        GLOBAL_LAST_NAME: "last_name",
        GLOBAL_AGE: "age",
        GLOBAL_SEX: "sex",
        GLOBAL_ADDRESS: "address",
        GLOBAL_ASIGNATURE: "subject",
        GLOBAL_PHONE: "phone"
    }

    for i, (field, label_text) in enumerate(fields):
        row = i // 2
        col = i % 2

        label = tk.Label(new_window, text=label_text, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
        label.grid(row=row, column=col * 2, padx=(10, 5), pady=5, sticky='e')

        entry = tk.Entry(new_window, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
        entry_value = str(teacher_data.get(data_keys[field], ""))
        entry.insert(0, entry_value)
        entry.grid(row=row, column=(col * 2) + 1, padx=(0, 10), pady=5, sticky='w')
        entries[field] = entry

    save_button = tk.Button(new_window, text=GLOBAL_BUTTON_SAVE, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                            command=lambda: update_teacher(tree, selected_item, 
                                                           entries[GLOBAL_TABLE_NIT].get(),
                                                           entries[GLOBAL_TABLE_NAME].get(),
                                                           entries[GLOBAL_LAST_NAME].get(),
                                                           entries[GLOBAL_AGE].get(),
                                                           entries[GLOBAL_SEX].get(),
                                                           entries[GLOBAL_ADDRESS].get(),
                                                           entries[GLOBAL_ASIGNATURE].get(),
                                                           entries[GLOBAL_PHONE].get(),
                                                           new_window))
    save_button.grid(row=(len(fields) // 2) + 1, column=1, pady=10, columnspan=3)

    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)

def open_teacher_details(tree, selected_item):
    if not selected_item or not tree.exists(selected_item):
        messagebox.showerror("Error", "No se ha seleccionado ningún docente válido.")
        return

    teacher_id = tree.item(selected_item, 'values')[0]

    success, teacher_data = get_teacher_details(teacher_id)
    if not success:
        messagebox.showerror("Error", teacher_data)
        return

    details_window = tk.Toplevel()
    details_window.title("Detalles del Docente")
    details_window.geometry("400x200")
    details_window.configure(bg=BACKGROUND_COLOR)

    data_keys = {
        "id_number": "Cédula",
        "first_name": "Nombres",
        "last_name": "Apellido",
        "age": "Edad",
        "sex": "Sexo",
        "address": "Dirección",
        "subject": "Asignatura",
        "phone": "Teléfono"
    }

    for i, (key, label_text) in enumerate(data_keys.items()):
        value = teacher_data.get(key, "N/A")
        row = i // 2
        col = i % 2

        label = tk.Label(details_window, text=f"{label_text}: {value}", bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=("Helvetica", 12))
        label.grid(row=row, column=col * 2, padx=(10, 5), pady=5, sticky='e')

    close_button = tk.Button(details_window, text="Cerrar", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, command=details_window.destroy)
    close_button.grid(row=(len(data_keys) // 2) + 1, column=0, pady=10, columnspan=8)

    close_button.bind("<Enter>", on_enter)
    close_button.bind("<Leave>", on_leave)

def confirm_delete_teacher(tree, selected_item, id_number):
    confirm_window = tk.Toplevel()
    confirm_window.title(GLOBAL_CONFIRM_DELETE)
    confirm_window.geometry("250x100")
    confirm_window.configure(bg=BACKGROUND_COLOR)

    message_label = tk.Label(confirm_window, text=f"¿Confirmar eliminación del docente {id_number}?", bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
    message_label.pack(pady=10)

    def delete_teacher():
        teacher_id = tree.item(selected_item, 'values')[0]
        success, message = remove_teacher(teacher_id)
        if success:
            tree.delete(selected_item)
            print(f"Docente con cédula {id_number} eliminado.")
        else:
            messagebox.showerror("Error", message)
        confirm_window.destroy()

    yes_button = tk.Button(confirm_window, text=GLOBAL_BUTTON_CONFIRM, command=delete_teacher)
    yes_button.pack(side="left", padx=(10, 5), pady=10)

    no_button = tk.Button(confirm_window, text=GLOBAL_BUTTON_CANCEL, command=confirm_window.destroy)
    no_button.pack(side="right", padx=(5, 10), pady=10)

def open_attendance_form(tree, selected_item):
    teacher_id = tree.item(selected_item, 'values')[0]
    
    success, teacher_data = get_teacher_details(teacher_id)
    if not success:
        messagebox.showerror("Error", teacher_data)
        return

    attendance_window = tk.Toplevel()
    attendance_window.title("Registrar Asistencia")
    attendance_window.geometry("300x275")
    attendance_window.configure(bg=BACKGROUND_COLOR)

    # Campos de entrada
    entry_frame = tk.Frame(attendance_window, bg=BACKGROUND_COLOR)
    entry_frame.pack(pady=10)

    labels = ["Cédula", "Nombre", "Asignatura", "Fecha"]
    entries = {}

    for i, label_text in enumerate(labels):
        label = tk.Label(entry_frame, text=label_text, bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
        label.grid(row=i, column=0, padx=5, pady=5, sticky='e')

        entry = tk.Entry(entry_frame, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, relief="flat")
        entry.grid(row=i, column=1, padx=5, pady=5, sticky='w')
        entries[label_text] = entry

    # Asignar valores por defecto, accediendo a teacher_data como diccionario
    entries["Cédula"].insert(0, teacher_data.get("id_number", "N/A"))
    entries["Nombre"].insert(0, teacher_data.get("first_name", "N/A"))
    entries["Asignatura"].insert(0, teacher_data.get("subject", "N/A"))  # Usar N/A si no hay asignatura

    # El usuario ahora podrá ingresar manualmente la fecha, se deja vacío el campo para que lo rellene
    entries["Fecha"].insert(0, "")  # Campo de fecha en blanco para que el usuario lo complete

    # Opción para marcar asistencia
    attendance_frame = tk.Frame(attendance_window, bg=BACKGROUND_COLOR)
    attendance_frame.pack(pady=10)

    attendance_label = tk.Label(attendance_frame, text="¿Asistió?", bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
    attendance_label.pack(side="left", padx=5)

    attendance_var = tk.StringVar(value="No")
    yes_radio = tk.Radiobutton(attendance_frame, text="Sí", variable=attendance_var, value="Sí", bg=BACKGROUND_COLOR)
    no_radio = tk.Radiobutton(attendance_frame, text="No", variable=attendance_var, value="No", bg=BACKGROUND_COLOR)

    yes_radio.pack(side="left", padx=5)
    no_radio.pack(side="left", padx=5)

    # Botón para registrar asistencia
    def register_attendance():
        attendance_status = attendance_var.get()
        teacher_data_list = list(teacher_data.values())  # Obtener los valores del diccionario teacher_data como lista

        # Obtener la fecha ingresada por el usuario
        entered_date = entries["Fecha"].get()
        if not entered_date:
            messagebox.showerror("Error", "Por favor ingrese una fecha válida.")
            return

        # Añadir la asistencia y la fecha ingresada a la lista
        teacher_data_list.append(entered_date)
        teacher_data_list.append(attendance_status)

        # Actualiza la columna de asistencia en la tabla con la nueva fecha y estado de asistencia
        tree.item(selected_item, values=teacher_data_list)

        # Mostrar messagebox confirmando el registro
        messagebox.showinfo("Registro de Asistencia", f"Asistencia del docente {teacher_data.get('first_name', 'N/A')} marcada como: {attendance_status} en la fecha: {entered_date}")
        attendance_window.destroy()

    register_button = tk.Button(attendance_window, text="Registrar", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR,
                                command=register_attendance)
    register_button.pack(pady=10)

# Handles

def on_click_action(tree, edit_button, delete_button, details_button, attendance_button, reports_button):
    selected_item = tree.selection()
    if selected_item:
        selected_teacher = tree.item(selected_item, 'values')
        edit_button.config(state="normal", command=lambda: open_edit_teacher_form(tree, selected_item))
        delete_button.config(state="normal", command=lambda: confirm_delete_teacher(tree, selected_item, selected_teacher[0]))
        details_button.config(state="normal", command=lambda: open_teacher_details(tree, selected_item))
        attendance_button.config(state="normal", command=lambda: open_attendance_form(tree, selected_item))
    else:
        edit_button.config(state="disabled")
        delete_button.config(state="disabled")
        details_button.config(state="disabled")
        attendance_button.config(state="disabled")

def on_enter(event):
    event.widget['background'] = BUTTON_COLOR_HOVER

def on_leave(event):
    event.widget['background'] = BUTTON_COLOR