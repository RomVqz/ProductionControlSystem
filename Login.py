import tkinter as tk
from tkinter import messagebox
import os

# Base de datos simulada con usuarios y contraseñas
USERS = {
    "admin": "password123",
    "user1": "mypassword"
}

# Función para validar el login
def validate_login(username, password):
    if username in USERS and USERS[username] == password:
        return True
    return False

# Función para manejar el evento de login
def login():
    username = entry_username.get()
    password = entry_password.get()

    if validate_login(username, password):
        messagebox.showinfo("Login exitoso", f"¡Bienvenido {username}!")
        login_window.destroy()  # Cierra la ventana de login
        open_main_app()  # Llama al main.py para iniciar la app principal
    else:
        messagebox.showerror("Error de Login", "Usuario o contraseña incorrectos")

# Función para abrir la ventana principal desde main.py
def open_main_app():
    os.system("python gui/windows/main.py")

# Crear la ventana de login
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x200")

# Etiquetas y entradas de texto para usuario y contraseña
label_username = tk.Label(login_window, text="Usuario:")
label_username.pack(pady=10)
entry_username = tk.Entry(login_window)
entry_username.pack(pady=5)

label_password = tk.Label(login_window, text="Contraseña:")
label_password.pack(pady=10)
entry_password = tk.Entry(login_window, show="*")  # Campo de texto para la contraseña
entry_password.pack(pady=5)

# Botón para iniciar sesión
login_button = tk.Button(login_window, text="Iniciar sesión", command=login)
login_button.pack(pady=20)

# Ejecutar la ventana de login
login_window.mainloop()
