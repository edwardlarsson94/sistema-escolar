import tkinter as tk
from tkinter import ttk, messagebox
from api.controllers.studentController import get_all_students
from components.Table import populate_table
from components.Tabs import create_student_tab, create_teacher_tab
from constants.Colors import BACKGROUND_COLOR, BUTTON_COLOR, BUTTON_TEXT_COLOR

def show_home_view():
    home_window = tk.Tk()
    home_window.title("Home")
    home_window.geometry("600x600")
    home_window.configure(bg=BACKGROUND_COLOR)

    top_frame = tk.Frame(home_window, bg=BACKGROUND_COLOR)
    top_frame.pack(side="top", fill="x", padx=10, pady=10)
    
    # Campo de entrada para el número de cédula
    cedula_year_entry = tk.Entry(top_frame, width=15)
    cedula_year_entry.pack(side="left", padx=5)
    cedula_year_entry.insert(0, "Cédula o Año")  # Texto de marcador de posición
    cedula_year_entry.bind("<FocusIn>", lambda e: clear_placeholder(cedula_year_entry))  # Limpiar el marcador de posición al hacer clic

    notebook = ttk.Notebook(home_window)
    notebook.pack(expand=True, fill='both')

    student_tab, student_tree = create_student_tab(notebook)
    
    search_button = tk.Button(top_frame, text="Buscar", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", command=lambda: search_action(cedula_year_entry.get(),  student_tree))
    search_button.pack(side="left", padx=5)

    create_teacher_tab(notebook)

    logout_button = tk.Button(top_frame, text="Cerrar Sesión", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", command=lambda: logout(home_window))
    logout_button.pack(side="right", padx=5)

    home_window.mainloop()

def clear_placeholder(entry):
    """Limpiar el marcador de posición si el campo tiene ese texto."""
    if entry.get() == "Número de Cédula":
        entry.delete(0, tk.END)

def logout(window):
    window.destroy()
    from src.modules.login.views.Login import create_login_view
    root = tk.Tk()
    create_login_view(root)
    root.mainloop()

def search_action(cedula_year, tree):
    filter_table(tree, cedula_year)

def filter_table(tree, cedula_year):
    # Limpiar la tabla
    for item in tree.get_children():
        tree.delete(item)

    # Obtener la lista de estudiantes
    success, students = get_all_students()
    
    if success:
        found = False
        # Filtrar por cédula o por año
        for student in students:
            if student['id_number'] == cedula_year or student['current_year'] == cedula_year:
                found = True
                tree.insert("", "end", values=(
                    student['student_id'],
                    student['id_number'],
                    student['first_name'],
                    student['last_name'],
                    student['current_year'],
                ))

        # Si no se encuentra ningún estudiante, mostrar todos los estudiantes
        if not found:
            messagebox.showwarning("Resultado de búsqueda", "Estudiante no encontrado. Mostrando todos los estudiantes.")
            populate_table(tree)
    else:
        messagebox.showerror("Error", "No se pudo obtener la información de los estudiantes.")