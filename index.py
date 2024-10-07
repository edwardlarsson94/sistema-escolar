import tkinter as tk
from src.modules.login.views.Login import create_login_view
from api.models.userModel import get_user
from database.connection import get_db_connection

if __name__ == "__main__":
    windows = tk.Tk()
    create_login_view(windows)
    connection = get_db_connection()
    user = get_user(connection)
    windows.mainloop()