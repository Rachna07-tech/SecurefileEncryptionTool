import tkinter as tk
from tkinter import filedialog, messagebox

from encrypt import encrypt_file
from decrypt import decrypt_file
from key_manager import generate_key

selected_file = ""

def browse_file():
    global selected_file
    selected_file = filedialog.askopenfilename()

    if selected_file:
        file_label.config(text=selected_file)

def create_key():
    generate_key()
    messagebox.showinfo(
        "Success",
        "Encryption key generated successfully!"
    )

def encrypt():
    if selected_file == "":
        messagebox.showwarning(
            "Warning",
            "Please select a file."
        )
        return

    try:
        output = encrypt_file(selected_file)

        messagebox.showinfo(
            "Success",
            f"File encrypted successfully!\n\nSaved at:\n{output}"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )
def decrypt():
    if selected_file == "":
        messagebox.showwarning(
            "Warning",
            "Please select a file."
        )
        return

    try:
        output = decrypt_file(selected_file)

        messagebox.showinfo(
            "Success",
            f"File decrypted successfully!\n\nSaved at:\n{output}"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )

root = tk.Tk()

root.title("Secure File Encryption Tool")

root.geometry("700x450")
root.resizable(False, False)
root.configure(bg="#E8F0FE")

title = tk.Label(
    root,
    text="Secure File Encryption Tool",
    font=("Arial", 22, "bold"),
    bg="#E8F0FE",
    fg="#1A237E"
)

title.pack(pady=20)

browse_btn = tk.Button(
    root,
    text="Browse File",
    width=20,
    bg="#1976D2",
    fg="white",
    font=("Arial", 10, "bold"),
    command=browse_file
)

browse_btn.pack(pady=10)
info = tk.Label(
    root,
    text="Encrypt and decrypt files securely using AES (Fernet).",
    font=("Arial", 10)
)

info.pack()

file_label = tk.Label(
    root,
    text="No File Selected",
    wraplength=500
)

file_label.pack()

key_btn = tk.Button(
    root,
    text="Generate Key",
    width=20,
    command=create_key
)

key_btn.pack(pady=10)

encrypt_btn = tk.Button(
    root,
    text="Encrypt File",
    width=20,
    command=encrypt
)

encrypt_btn.pack(pady=10)

decrypt_btn = tk.Button(
    root,
    text="Decrypt File",
    width=20,
    command=decrypt
)

decrypt_btn.pack(pady=10)

exit_btn = tk.Button(
    root,
    text="Exit",
    width=20,
    command=root.destroy
)

exit_btn.pack(pady=20)

root.mainloop()