import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "Done" if task["completed"] else "Not Done"
        task_listbox.insert(tk.END, f"{task['task']} [{status}]")

def mark_task_completed():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task = tasks[selected_task_index[0]]
        task["completed"] = True
        update_task_list()

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_task_list()

app = tk.Tk()
app.title("To-Do List App")

task_entry = tk.Entry(app, width=50)
task_entry.pack()

add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack()

task_listbox = tk.Listbox(app, width=50, height=10)
task_listbox.pack()

complete_button = tk.Button(app, text="Mark as Completed", command=mark_task_completed)
complete_button.pack()

delete_button = tk.Button(app, text="Delete Task", command=delete_task)
delete_button.pack()

app.mainloop()
