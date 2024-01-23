import tkinter as tk
from tkinter import messagebox


class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        self.contacts = {}

        self.name_entry = tk.Entry(root, width=30)
        self.phone_entry = tk.Entry(root, width=30)
        self.email_entry = tk.Entry(root, width=30)
        self.address_entry = tk.Entry(root, width=30)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)

        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="E")
        tk.Label(root, text="Phone:").grid(row=1, column=0, padx=10, pady=5, sticky="E")
        tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky="E")
        tk.Label(root, text="Address:").grid(row=3, column=0, padx=10, pady=5, sticky="E")

        self.add_button.grid(row=4, column=1, pady=10)
        self.view_button.grid(row=5, column=1, pady=10)
        self.search_button.grid(row=6, column=1, pady=10)
        self.update_button.grid(row=7, column=1, pady=10)
        self.delete_button.grid(row=8, column=1, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        if name:
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()

            contact_details = {'Phone': phone, 'Email': email, 'Address': address}
            self.contacts[name] = contact_details

            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Name field cannot be empty!")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Information", "No contacts available.")
        else:
            contact_list = "\n".join([f"{name}: {details['Phone']}" for name, details in self.contacts.items()])
            messagebox.showinfo("Contacts", contact_list)

    def search_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            details = self.contacts[name]
            messagebox.showinfo("Contact Details",
        f"Name: {name}\nPhone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}")
        else:
            messagebox.showinfo("Contact Not Found", f"Contact with name {name} not found.")

    def update_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()

            self.contacts[name]['Phone'] = phone
            self.contacts[name]['Email'] = email
            self.contacts[name]['Address'] = address

            messagebox.showinfo("Success", "Contact updated successfully!")
            self.clear_entries()
        else:
            messagebox.showinfo("Contact Not Found", f"Contact with name {name} not found.")

    def delete_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", f"Contact {name} deleted successfully!")

            # Clear entry fields after deleting a contact
            self.clear_entries()
        else:
            messagebox.showinfo("Contact Not Found", f"Contact with name {name} not found.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
