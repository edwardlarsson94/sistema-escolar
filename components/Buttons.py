import tkinter as tk
from constants.Colors import BUTTON_COLOR, BUTTON_TEXT_COLOR, BUTTON_COLOR_HOVER

def on_enter(e):
    e.widget['background'] = BUTTON_COLOR_HOVER

def on_leave(e):
    e.widget['background'] = BUTTON_COLOR

def create_login_button(window, command, entry_user, entry_password):
    button_login = tk.Button(window, text="Sign in", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, font=("Helvetica", 12, "bold"), relief="flat")
    button_login.pack(pady=20, ipadx=80, ipady=10)

    button_login.config(command=command)
