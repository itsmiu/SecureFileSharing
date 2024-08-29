import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog, messagebox
from file_encryption import encrypt_file, decrypt_file, generate_key

def authenticate(username, password):
    valid_username = "user"
    valid_password = "password"
    return username == valid_username and password == valid_password

def on_login():
    username = username_entry.get()
    password = password_entry.get()

    if authenticate(username, password):
        messagebox.showinfo("Login Successful", "You are now logged in.")
        app_login.destroy()
        create_file_sharing_ui()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def create_file_sharing_ui():
    global app_file_sharing
    app_file_sharing = ctk.CTk()
    app_file_sharing.title("File Sharing")
    app_file_sharing.geometry("500x400")

    instructions_label = ctk.CTkLabel(app_file_sharing, text="Secure File Sharing System", wraplength=450)
    instructions_label.pack(pady=10)

    encrypt_button = ctk.CTkButton(app_file_sharing, text="Encrypt File", command=encrypt_file_ui)
    encrypt_button.pack(pady=10)

    decrypt_button = ctk.CTkButton(app_file_sharing, text="Decrypt File", command=decrypt_file_ui)
    decrypt_button.pack(pady=10)

    app_file_sharing.mainloop()

def encrypt_file_ui():
    file_path = filedialog.askopenfilename(title="Select File to Encrypt")
    if file_path:
        encrypt_file(file_path)
        messagebox.showinfo("Success", f"File '{file_path}' encrypted successfully.")

def decrypt_file_ui():
    file_path = filedialog.askopenfilename(title="Select File to Decrypt")
    if file_path:
        decrypt_file(file_path)
        messagebox.showinfo("Success", f"File '{file_path}' decrypted successfully.")

# Setup CustomTkinter application for login
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app_login = ctk.CTk()
app_login.title("File Sharing Login")
app_login.geometry("400x300")

tk.Label(app_login, text="Username").pack(pady=5)
username_entry = tk.Entry(app_login)
username_entry.pack(pady=5)

tk.Label(app_login, text="Password").pack(pady=5)
password_entry = tk.Entry(app_login, show="*")
password_entry.pack(pady=5)

login_button = tk.Button(app_login, text="Login", command=on_login)
login_button.pack(pady=10)

app_login.mainloop()
