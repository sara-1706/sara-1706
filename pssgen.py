import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate a random password
def generate_password():
    try:
        length = int(length_entry.get())  # Get the length from the user input
        if length < 1:
            raise ValueError("Password length must be greater than 0")
        
        # Define characters for the password
        all_characters = string.ascii_letters + string.digits + string.punctuation
        
        # Generate password of the specified length
        password = ''.join(random.choices(all_characters, k=length))
        
        # Display the password in green color
        result_label.config(text=f"Generated Password: {password}", fg="green")
    
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# Create the main window
root = tk.Tk()
root.title("Colorful Password Generator")
root.geometry("400x300")
root.config(bg="#F0F8FF")

# Create a label for instruction with styling
label = tk.Label(root, text="Enter the desired password length:", font=("Arial", 14), bg="#F0F8FF", fg="#4B0082")
label.pack(pady=10)

# Create an entry field for password length with styling
length_entry = tk.Entry(root, font=("Arial", 12), bg="#E6E6FA", bd=2)
length_entry.pack(pady=5)

# Create a button to generate password with styling
generate_button = tk.Button(root, text="Generate Password", font=("Arial", 14), command=generate_password, bg="#8A2BE2", fg="white", bd=2)
generate_button.pack(pady=15)

# Create a label to display the generated password with styling
result_label = tk.Label(root, text="Generated Password: ", font=("Arial", 12), bg="#F0F8FF", fg="#4B0082")
result_label.pack(pady=10)

# Run the application
root.mainloop()
