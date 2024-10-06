import tkinter as tk
from modules.login.views.Login import create_login_view

if __name__ == "__main__":
    windows = tk.Tk()
    create_login_view(windows)
    windows.mainloop()