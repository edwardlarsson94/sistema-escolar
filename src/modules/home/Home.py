import tkinter as tk
from constants.Colors import BACKGROUND_COLOR, TITLE_COLOR

def show_home_view():
    home_window = tk.Tk()
    home_window.title("Home")
    home_window.geometry("400x600")
    home_window.configure(bg=BACKGROUND_COLOR)

    label_title = tk.Label(home_window, text="Welcome to the Home Page!", bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=("Helvetica", 24, "bold"))
    label_title.pack(pady=20)

    label_content = tk.Label(home_window, text="¡Has iniciado sesión correctamente!", bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=("Helvetica", 14))
    label_content.pack(pady=20)

    home_window.mainloop()
