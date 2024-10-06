import tkinter as tk
from tkinter import font
from modules.login.services.LoginService import verify_login
from constants.Colors import BACKGROUND_COLOR, ENTRY_BACKGROUND, ENTRY_FOREGROUND, LABEL_COLOR, TITLE_COLOR, SUBTITLE_COLOR
from components.Buttons import create_login_button

def create_login_view(window):
    window.title("Welcome Back!")
    window.geometry("400x500")
    window.configure(bg=BACKGROUND_COLOR)

    title_font = font.Font(family="Helvetica", size=24, weight="bold")
    subtitle_font = font.Font(family="Helvetica", size=10)

    label_title = tk.Label(window, text="Welcome Back!", bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=title_font)
    label_title.pack(pady=20)

    label_subtitle = tk.Label(window, text="Welcome back, we missed you", bg=BACKGROUND_COLOR, fg=SUBTITLE_COLOR, font=subtitle_font)
    label_subtitle.pack(pady=5)

    tk.Label(window, bg=BACKGROUND_COLOR).pack(pady=10)

    label_user = tk.Label(window, text="Username:", bg=BACKGROUND_COLOR, fg=LABEL_COLOR, font=("Helvetica", 12))
    label_user.pack(pady=5)

    entry_user = tk.Entry(window, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, font=("Helvetica", 12), insertbackground=ENTRY_FOREGROUND, relief="flat")
    entry_user.pack(ipady=8, ipadx=10, pady=10)

    label_password = tk.Label(window, text="Password:", bg=BACKGROUND_COLOR, fg=LABEL_COLOR, font=("Helvetica", 12))
    label_password.pack(pady=5)

    entry_password = tk.Entry(window, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, show="*", font=("Helvetica", 12), insertbackground=ENTRY_FOREGROUND, relief="flat")
    entry_password.pack(ipady=8, ipadx=10, pady=10)

    create_login_button(window, verify_login, entry_user, entry_password)
