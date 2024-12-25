import tkinter as tk
from tkinter import messagebox, simpledialog

# Contact dictionary to store contact details
contacts = {}

# Function to add a new contact
def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter Name:")
    if not name:
        return
    phone = simpledialog.askstring("Add Contact", "Enter Phone Number:")
    email = simpledialog.askstring("Add Contact", "Enter Email:")
    address = simpledialog.askstring("Add Contact", "Enter Address:")
    if not phone:
        messagebox.showerror("Error", "Phone number is required.")
        return
    
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
    refresh_contact_list()

# Function to view all contacts
def refresh_contact_list():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name} ({details['Phone']})")

# Function to search for a contact
def search_contact():
    search_query = simpledialog.askstring("Search Contact", "Enter Name or Phone Number:")
    if not search_query:
        return
    
    results = [name for name, details in contacts.items() 
               if search_query.lower() in name.lower() or search_query in details['Phone']]
    
    if results:
        result_text = "\n".join([f"{name} - {contacts[name]['Phone']}" for name in results])
        messagebox.showinfo("Search Results", result_text)
    else:
        messagebox.showinfo("Search Results", "No contact found.")

# Function to update a contact
def update_contact():
    name = simpledialog.askstring("Update Contact", "Enter Name of Contact to Update:")
    if name not in contacts:
        messagebox.showerror("Error", "Contact not found.")
        return
    
    phone = simpledialog.askstring("Update Contact", "Enter New Phone Number:", initialvalue=contacts[name]["Phone"])
    email = simpledialog.askstring("Update Contact", "Enter New Email:", initialvalue=contacts[name]["Email"])
    address = simpledialog.askstring("Update Contact", "Enter New Address:", initialvalue=contacts[name]["Address"])
    
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    messagebox.showinfo("Success", f"Contact '{name}' updated successfully!")
    refresh_contact_list()

# Function to delete a contact
def delete_contact():
    name = simpledialog.askstring("Delete Contact", "Enter Name of Contact to Delete:")
    if name not in contacts:
        messagebox.showerror("Error", "Contact not found.")
        return
    
    del contacts[name]
    messagebox.showinfo("Success", f"Contact '{name}' deleted successfully!")
    refresh_contact_list()

# Create the main window
root = tk.Tk()
root.title("Contact Management System")
root.geometry("400x400")

# Buttons for actions
add_button = tk.Button(root, text="Add Contact", command=add_contact, bg="#8A2BE2", fg="white", font=("Arial", 12))
add_button.pack(pady=5)

view_button = tk.Button(root, text="View All Contacts", command=refresh_contact_list, bg="#8A2BE2", fg="white", font=("Arial", 12))
view_button.pack(pady=5)

search_button = tk.Button(root, text="Search Contact", command=search_contact, bg="#8A2BE2", fg="white", font=("Arial", 12))
search_button.pack(pady=5)

update_button = tk.Button(root, text="Update Contact", command=update_contact, bg="#8A2BE2", fg="white", font=("Arial", 12))
update_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact, bg="#8A2BE2", fg="white", font=("Arial", 12))
delete_button.pack(pady=5)

# Listbox to display contact names and numbers
contact_list = tk.Listbox(root, font=("Arial", 12), height=10, width=40)
contact_list.pack(pady=10)

# Run the application
root.mainloop()
