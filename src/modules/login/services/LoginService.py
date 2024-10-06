def verify_login(window, entry_user, entry_password, show_home_view):
    user = entry_user.get()
    password = entry_password.get()
    
    if user == "admin" and password == "1234":
        window.destroy()
        show_home_view()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")
