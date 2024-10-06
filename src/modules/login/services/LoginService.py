from tkinter import messagebox

def verify_login(entry_user, entry_password):
    user = entry_user.get()
    password = entry_password.get()
    
    if user == "admin" and password == "1234":
        messagebox.showinfo("Login exitoso", "¡Bienvenido!")
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")
