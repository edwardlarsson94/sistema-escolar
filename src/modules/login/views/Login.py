import tkinter as tk
from modules.login.services.LoginService import verify_login

def create_login_view(window):
    window.title("Sistema de Login")
    window.geometry("300x150")

    label_user = tk.Label(window, text="Usuario:")
    label_user.pack(pady=5)

    entry_user = tk.Entry(window)
    entry_user.pack(pady=5)

    label_password = tk.Label(window, text="Contraseña:")
    label_password.pack(pady=5)

    entry_password = tk.Entry(window, show="*")
    entry_password.pack(pady=5)

    button_login = tk.Button(window, text="Iniciar sesión", 
                             command=lambda: verify_login(entry_user, entry_password))
    button_login.pack(pady=10)
