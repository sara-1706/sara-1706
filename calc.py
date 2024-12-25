import tkinter as tk

def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for displaying calculations
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Create buttons and add them to the window
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), bg="orange", command=calculate)
    elif text == "C":
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), bg="green", command=clear)
    else:
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=lambda t=text: click_button(t))
    button.grid(row=row, column=col)

# Start the main loop
root.mainloop()
