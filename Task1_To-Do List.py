import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry_task.delete(0, 'end')
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def edit_task():
    selected_task = list_tasks.curselection()
    if selected_task:
        index = selected_task[0]
        entry_task.delete(0, 'end')
        entry_task.insert(0, tasks[index])
    else:
        messagebox.showwarning("Warning", "Please select a task to edit!")

def save_edit():
    selected_task = list_tasks.curselection()
    if selected_task:
        index = selected_task[0]
        updated_task = entry_task.get()
        tasks[index] = updated_task
        update_listbox()
        entry_task.delete(0, 'end')
    else:
        messagebox.showwarning("Warning", "Please select a task to save edit!")

def delete_task():
    selected_task = list_tasks.curselection()
    if selected_task:
        index = selected_task[0]
        del tasks[index]
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def update_listbox():
    list_tasks.delete(0, 'end')
    for index, task in enumerate(tasks, start=1):
        list_tasks.insert('end', f"{index}. {task}")

# Create the main window
root = tk.Tk()
root.title("TO-DO List")

tasks = []

# Task input
entry_task = tk.Entry(root, width=50)
entry_task.pack()

# Add Task button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# List of tasks
list_tasks = tk.Listbox(root, width=50)
list_tasks.pack()

# Edit Task button
edit_button = tk.Button(root, text="Edit Task", command=edit_task)
edit_button.pack()

# Save Edit button
save_button = tk.Button(root, text="Save Edit", command=save_edit)
save_button.pack()

# Delete Task button
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

root.mainloop()
