import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def generate():
    try:
        length_value = int(length_entry.get())
        if length_value < 5:
            messagebox.showwarning("Warning", "Password length must be at least 5.")
            return
        password = generate_password(length_value)
        result_label.config(text=password)
        copy_button.config(state="normal") 
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def copy_password():
    password = result_label.cget("text")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title('Password Generator')
root.geometry('350x250')
root.resizable(False, False)

tk.Label(root, text="Enter password length:").pack(pady=5)
length_entry = tk.Entry(root, width=20)
length_entry.pack(pady=5)

tk.Button(root, text="Generate", command=generate).pack(pady=10)

result_label = tk.Label(root, text="", font=('Arial', 12))
result_label.pack(pady=10)

copy_button = tk.Button(root, text="Copy", command=copy_password, state="disabled")
copy_button.pack(pady=5)

root.mainloop()
