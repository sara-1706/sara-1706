import tkinter as tk
from tkinter import messagebox
import json

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.configure(bg="#f7f3e9")

        self.tasks = []
        self.load_tasks()

        # Title Label
        self.title_label = tk.Label(root, text="To-Do List", font=("Arial", 18, "bold"), bg="#f7f3e9", fg="#3e3b47")
        self.title_label.pack(pady=10)

        # Input Frame
        self.input_frame = tk.Frame(root, bg="#f7f3e9")
        self.input_frame.pack()

        self.task_entry = tk.Entry(self.input_frame, width=30, font=("Arial", 12))
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(
            self.input_frame, text="Add Task", bg="#8bc34a", fg="white",
            font=("Arial", 12, "bold"), command=self.add_task, relief="ridge"
        )
        self.add_button.grid(row=0, column=1, padx=10)

        # Task Listbox
        self.task_list = tk.Listbox(root, width=50, height=15, font=("Arial", 12), bg="#ffffff", fg="#333333", selectbackground="#8bc34a")
        self.task_list.pack(pady=10)

        # Action Buttons
        self.button_frame = tk.Frame(root, bg="#f7f3e9")
        self.button_frame.pack(pady=10)

        self.complete_button = tk.Button(
            self.button_frame, text="Mark Completed", bg="#2196f3", fg="white",
            font=("Arial", 12, "bold"), command=self.mark_completed, relief="ridge"
        )
        self.complete_button.grid(row=0, column=0, padx=10)

        self.delete_button = tk.Button(
            self.button_frame, text="Delete Task", bg="#f44336", fg="white",
            font=("Arial", 12, "bold"), command=self.delete_task, relief="ridge"
        )
        self.delete_button.grid(row=0, column=1, padx=10)

        self.save_button = tk.Button(
            self.button_frame, text="Save Tasks", bg="#ff9800", fg="white",
            font=("Arial", 12, "bold"), command=self.save_tasks, relief="ridge"
        )
        self.save_button.grid(row=0, column=2, padx=10)

        self.refresh_list()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.task_entry.delete(0, tk.END)
            self.refresh_list()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def mark_completed(self):
        try:
            selected_index = self.task_list.curselection()[0]
            self.tasks[selected_index]["completed"] = True
            self.refresh_list()
        except IndexError:
            messagebox.showwarning("Warning", "No task selected!")

    def delete_task(self):
        try:
            selected_index = self.task_list.curselection()[0]
            del self.tasks[selected_index]
            self.refresh_list()
        except IndexError:
            messagebox.showwarning("Warning", "No task selected!")

    def refresh_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            status = "[Done]" if task["completed"] else "[Pending]"
            self.task_list.insert(tk.END, f"{task['task']} {status}")

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)
        messagebox.showinfo("Info", "Tasks saved successfully!")

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
