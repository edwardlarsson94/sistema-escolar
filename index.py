import tkinter as tk
from tkinter import messagebox

def verify_login():
    user = entry_user.get()
    password = entry_password.get()
    
    if user == "admin" and password == "1234":
        messagebox.showinfo("Login exitoso", "¡Bienvenido!")
    else:
        messagebox.showerror("Error", "user o contraseña incorrectos")

windows = tk.Tk()
windows.title("Sistema de Login")
windows.geometry("300x150")

label_user = tk.Label(windows, text="user:")
label_user.pack(pady=5)

entry_user = tk.Entry(windows)
entry_user.pack(pady=5)

label_password = tk.Label(windows, text="Contraseña:")
label_password.pack(pady=5)

entry_password = tk.Entry(windows, show="*")
entry_password.pack(pady=5)

button_login = tk.Button(windows, text="Iniciar sesión", command=verify_login)
button_login.pack(pady=10)

windows.mainloop()
