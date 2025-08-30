import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.contacts = load_contacts()

        # UI Elements
        self.listbox = tk.Listbox(root, width=50, height=15)
        self.listbox.pack(pady=10)

        self.add_btn = tk.Button(root, text="Add Contact", width=20, command=self.add_contact)
        self.add_btn.pack()

        self.edit_btn = tk.Button(root, text="Edit Selected", width=20, command=self.edit_contact)
        self.edit_btn.pack()

        self.delete_btn = tk.Button(root, text="Delete Selected", width=20, command=self.delete_contact)
        self.delete_btn.pack()

        self.refresh_btn = tk.Button(root, text="Refresh List", width=20, command=self.refresh_contacts)
        self.refresh_btn.pack()

        self.quit_btn = tk.Button(root, text="Save & Quit", width=20, command=self.quit_app)
        self.quit_btn.pack(pady=10)

        self.refresh_contacts()

    def refresh_contacts(self):
        self.listbox.delete(0, tk.END)
        for contact in self.contacts:
            display = f"{contact['name']} | {contact['phone']} | {contact['email']}"
            self.listbox.insert(tk.END, display)

    def add_contact(self):
        name = simpledialog.askstring("Name", "Enter name:")
        if not name: return
        phone = simpledialog.askstring("Phone", "Enter phone number:")
        if not phone: return
        email = simpledialog.askstring("Email", "Enter email address:")
        if not email: return
        self.contacts.append({"name": name, "phone": phone, "email": email})
        self.refresh_contacts()

    def edit_contact(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Select Contact", "Please select a contact to edit.")
            return
        index = selected[0]
        contact = self.contacts[index]

        name = simpledialog.askstring("Edit Name", "Enter new name:", initialvalue=contact['name'])
        if not name: return
        phone = simpledialog.askstring("Edit Phone", "Enter new phone number:", initialvalue=contact['phone'])
        if not phone: return
        email = simpledialog.askstring("Edit Email", "Enter new email address:", initialvalue=contact['email'])
        if not email: return

        self.contacts[index] = {"name": name, "phone": phone, "email": email}
        self.refresh_contacts()

    def delete_contact(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Select Contact", "Please select a contact to delete.")
            return
        index = selected[0]
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this contact?")
        if confirm:
            del self.contacts[index]
            self.refresh_contacts()

    def quit_app(self):
        save_contacts(self.contacts)
        self.root.quit()

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
