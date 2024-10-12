import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        messagebox.showwarning("Delete Error", "Please select a task to delete.")

def update_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        new_task = entry_task.get()
        if new_task != "":
            listbox_tasks.delete(task_index)
            listbox_tasks.insert(task_index, new_task)
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a new task.")
    except:
        messagebox.showwarning("Update Error", "Please select a task to update.")

def clear_all():
    listbox_tasks.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("To-do List")

# Add widgets
frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack()

button_add_task = tk.Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack()

button_update_task = tk.Button(root, text="Update Task", width=48, command=update_task)
button_update_task.pack()

button_delete_task = tk.Button(root, text="Delete Task", width=48, command=delete_task)
button_delete_task.pack()

button_clear_all = tk.Button(root, text="Clear All Tasks", width=48, command=clear_all)
button_clear_all.pack()

# Run the application
root.mainloop()
