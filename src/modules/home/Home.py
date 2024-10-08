import tkinter as tk
from tkinter import ttk
from constants.Colors import BACKGROUND_COLOR, BUTTON_COLOR, BUTTON_TEXT_COLOR, BUTTON_COLOR_HOVER, TITLE_COLOR
from components.Tabs import create_student_tab, create_teacher_tab

def show_home_view():
    home_window = tk.Tk()
    home_window.title("Home")
    home_window.geometry("600x500")
    home_window.configure(bg=BACKGROUND_COLOR)

    logout_button = tk.Button(home_window, text="Cerrar Sesión", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, relief="flat", 
                              command=lambda: logout(home_window))
    logout_button.pack(side="top", anchor="ne", padx=10, pady=10)

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
