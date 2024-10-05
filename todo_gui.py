import tkinter as tk
from tkinter import messagebox

def add_item():
    item = input_field.get()
    if item.strip()!= "":
        task_box.insert(tk.END,item) 
        input_field.delete(0,tk.END)
    else:
        messagebox.showerror("Error","Task cannot be empty!")  

def remove_item():
    try:
        selected_task = task_box.curselection()[0] 
        task_box.delete(selected_task)
    except IndexError:
        messagebox.showerror("Error","No task selected!")
        
app = tk.Tk()
app.title("Todo List using guisS")
input_field = tk.Entry(app, width=40)
input_field.grid(row=0, column=0, padx=10, pady=10)
add_btn = tk.Button(app, text="Add Task", width=15, command=add_item)
add_btn.grid(row=0, column=1, padx=10, pady=10)
task_box = tk.Listbox(app, height=10, width=50)
task_box.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
remove_btn = tk.Button(app, text="Remove Task", width=15, command=remove_item)
remove_btn.grid(row=2, column=0, columnspan=2, pady=10)
app.mainloop()
