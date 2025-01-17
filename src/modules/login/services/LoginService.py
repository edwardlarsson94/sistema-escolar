from api.controllers.userController import authenticate_user
from tkinter import messagebox

def verify_login(window, entry_user, entry_password, show_home_view):
    username = entry_user.get()
    password = entry_password.get()
    
    authenticated, user = authenticate_user(username, password)
    
    if authenticated:
        window.destroy()
        show_home_view()
    else:
        messagebox.showwarning("Credenciales Incorrectas", "El nombre de usuario o la contraseña son incorrectos.")
