# main.py
import tkinter as tk
from tkinter import ttk
from constants.Colors import BACKGROUND_COLOR
from components.Tabs import create_student_tab, create_teacher_tab

def show_home_view():
    home_window = tk.Tk()
    home_window.title("Home")
    home_window.geometry("600x500")
    home_window.configure(bg=BACKGROUND_COLOR)

    notebook = ttk.Notebook(home_window)
    notebook.pack(expand=True, fill='both')

    create_student_tab(notebook)
    create_teacher_tab(notebook)

    home_window.mainloop()