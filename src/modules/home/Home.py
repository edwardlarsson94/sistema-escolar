import tkinter as tk
from tkinter import ttk
from constants.Colors import BACKGROUND_COLOR, BUTTON_COLOR, BUTTON_TEXT_COLOR
from components.Tabs import create_student_tab, create_teacher_tab

def show_home_view():
    home_window = tk.Tk()
    home_window.title("Home")
    home_window.geometry("600x600")
    home_window.configure(bg=BACKGROUND_COLOR)

    top_frame = tk.Frame(home_window, bg=BACKGROUND_COLOR)
    top_frame.pack(side="top", fill="x", padx=10, pady=10)
    logout_button = tk.Button(top_frame, text="Cerrar Sesión", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", command=lambda: logout(home_window))
    logout_button.pack(side="right", padx=5)
    search_button = tk.Button(top_frame, text="Buscar", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", command=search_action)
    search_button.pack(side="left", padx=5)
    notebook = ttk.Notebook(home_window)
    notebook.pack(expand=True, fill='both')

    create_student_tab(notebook)
    create_teacher_tab(notebook)

    home_window.mainloop()

def logout(window):
    window.destroy()
    from src.modules.login.views.Login import create_login_view
    root = tk.Tk()
    create_login_view(root)
    root.mainloop()
def search_action():
    print("Función de búsqueda ejecutada.")