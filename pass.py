import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    length = int(length_var.get())
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        password_var.set("Error: Select at least one character type")
    else:
        password = ''.join(random.choice(characters) for _ in range(length))
        password_var.set(password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x500")

length_var = tk.StringVar(value="12")
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
password_var = tk.StringVar()

ttk.Label(root, text="Password Length:").pack(pady=5)
ttk.Entry(root, textvariable=length_var, width=5).pack()

ttk.Checkbutton(root, text="Include Letters", variable=letters_var).pack(pady=5)
ttk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack(pady=5)
ttk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(pady=5)

ttk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

password_entry = ttk.Entry(root, textvariable=password_var, width=30)
password_entry.pack(pady=5)

ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)

root.mainloop()