import tkinter as tk
from tkinter import ttk, messagebox

class ContactBook:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")
        self.master.geometry("600x400")
        
        self.contacts = []
        
        self.create_widgets()
        
    def create_widgets(self):
        # Left frame for contact list and search
        left_frame = ttk.Frame(self.master, padding="10")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        ttk.Label(left_frame, text="Search:").pack(anchor=tk.W)
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.update_list)
        ttk.Entry(left_frame, textvariable=self.search_var).pack(fill=tk.X)
        
        self.contact_list = tk.Listbox(left_frame, width=40)
        self.contact_list.pack(fill=tk.BOTH, expand=True)
        self.contact_list.bind('<<ListboxSelect>>', self.on_select)
        
        # Right frame for contact details and actions
        right_frame = ttk.Frame(self.master, padding="10")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        fields = ['Name', 'Phone', 'Email', 'Address']
        self.entries = {}
        for field in fields:
            ttk.Label(right_frame, text=field).pack(anchor=tk.W)
            self.entries[field] = ttk.Entry(right_frame)
            self.entries[field].pack(fill=tk.X)
        
        ttk.Button(right_frame, text="Add/Update Contact", command=self.add_update_contact).pack(fill=tk.X, pady=5)
        ttk.Button(right_frame, text="Delete Contact", command=self.delete_contact).pack(fill=tk.X)
        
    def add_update_contact(self):
        name = self.entries['Name'].get()
        if not name:
            messagebox.showerror("Error", "Name is required")
            return
        
        contact = {field: self.entries[field].get() for field in self.entries}
        
        for i, existing_contact in enumerate(self.contacts):
            if existing_contact['Name'] == name:
                self.contacts[i] = contact
                break
        else:
            self.contacts.append(contact)
        
        self.update_list()
        self.clear_entries()
        
    def delete_contact(self):
        selection = self.contact_list.curselection()
        if not selection:
            messagebox.showerror("Error", "No contact selected")
            return
        
        index = selection[0]
        del self.contacts[index]
        self.update_list()
        self.clear_entries()
        
    def update_list(self, *args):
        search_term = self.search_var.get().lower()
        self.contact_list.delete(0, tk.END)
        for contact in self.contacts:
            if search_term in contact['Name'].lower() or search_term in contact['Phone']:
                self.contact_list.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")
                
    def on_select(self, event):
        selection = self.contact_list.curselection()
        if selection:
            index = selection[0]
            contact = self.contacts[index]
            for field in self.entries:
                self.entries[field].delete(0, tk.END)
                self.entries[field].insert(0, contact[field])
                
    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()