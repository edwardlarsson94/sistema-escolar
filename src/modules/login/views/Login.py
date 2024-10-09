import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from constants.Colors import BACKGROUND_COLOR, ENTRY_BACKGROUND, ENTRY_FOREGROUND, LABEL_COLOR, TITLE_COLOR, SUBTITLE_COLOR
from constants.Texts import GLOBAL_SISTEMA_ESCOLAR_TITLE, LOGIN_SISTEMA_ESCOLAR_SUBTITLE, LOGIN_LABEL_USER, LOGIN_LABEL_PASSWORD
from src.modules.login.services.LoginService import verify_login
from src.modules.home.Home import show_home_view
from components.ButtonLogin import create_login_button

def create_login_view(window):
    window.title(GLOBAL_SISTEMA_ESCOLAR_TITLE)
    window.geometry("500x600")
    window.configure(bg=BACKGROUND_COLOR)

    image_path = "assets/login/logo.png"
    img = Image.open(image_path)
    img = img.resize((250, 200), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(img)

    label_image = tk.Label(window, image=photo, bg=BACKGROUND_COLOR)
    label_image.image = photo
    label_image.pack(pady=20) 

    title_font = font.Font(family="Helvetica", size=24, weight="bold")
    subtitle_font = font.Font(family="Helvetica", size=10)

    label_title = tk.Label(window, text=GLOBAL_SISTEMA_ESCOLAR_TITLE, bg=BACKGROUND_COLOR, fg=TITLE_COLOR, font=title_font)
    label_subtitle = tk.Label(window, text=LOGIN_SISTEMA_ESCOLAR_SUBTITLE, bg=BACKGROUND_COLOR, fg=SUBTITLE_COLOR, font=subtitle_font)

    label_title.pack(pady=0) 
    label_subtitle.pack(pady=10) 

    label_user = tk.Label(window, text=LOGIN_LABEL_USER, bg=BACKGROUND_COLOR, fg=LABEL_COLOR, font=("Helvetica", 12))
    label_user.pack(pady=10)  

    entry_user = tk.Entry(window, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, font=("Helvetica", 12), insertbackground=ENTRY_FOREGROUND, relief="flat")
    entry_user.pack(ipady=8, ipadx=10, pady=10) 

    label_password = tk.Label(window, text=LOGIN_LABEL_PASSWORD, bg=BACKGROUND_COLOR, fg=LABEL_COLOR, font=("Helvetica", 12))
    label_password.pack(pady=10) 
    
    entry_password = tk.Entry(window, bg=ENTRY_BACKGROUND, fg=ENTRY_FOREGROUND, show="*", font=("Helvetica", 12), insertbackground=ENTRY_FOREGROUND, relief="flat")
    entry_password.pack(ipady=8, ipadx=10, pady=10)  
    
    create_login_button(window, lambda: verify_login(window, entry_user, entry_password, show_home_view), entry_user, entry_password)
