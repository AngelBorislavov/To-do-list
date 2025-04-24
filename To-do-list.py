from tkinter import *
import os

root = Tk()
root.title('To-do-list')
root.geometry('600x500')

tasks = []

TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from file when the app starts."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            lines = file.readlines()
            for line in lines:
                add_task(line.strip(), load=True)

def save_tasks():
    """Save tasks to a file."""
    with open(TASKS_FILE, 'w') as file:
        for task_frame in tasks:
            task_label = task_frame.winfo_children()[0]  # Getting the label inside the frame
            file.write(task_label.cget("text") + "\n")

def add_task(task_value=None, load=False):
    """Add a task to the list."""
    if not task_value:
        task_value = task_input.get().strip()

    if task_value == "":
        return

    task_input.delete(0, 'end')

    # Frame to hold the task label and delete button
    task_frame = Frame(root)
    task_frame.grid(row=len(tasks)+1, column=0, columnspan=2, sticky='we', padx=30, pady=2)

    task_label = Label(task_frame, text=task_value, anchor='w', font=24)
    task_label.pack(side='left', fill='x', expand=True)

    def delete_task():
        task_frame.destroy()
        tasks.remove(task_frame)
        save_tasks()  # Save tasks after deletion
        redraw_tasks()

    delete_button = Button(task_frame, text='Delete', command=delete_task)
    delete_button.pack(side='right', padx=5)

    tasks.append(task_frame)

    if not load:
        save_tasks()  # Save tasks after adding a new one

def redraw_tasks():
    """Rearrange tasks when one is deleted."""
    for index, frame in enumerate(tasks):
        frame.grid(row=index + 1, column=0, columnspan=2, sticky='we', padx=30, pady=2)

# Create widgets
task_input = Entry(root, width=40, font=24)
add_button = Button(root, text='Add', width=20, command=add_task)

# Show widgets
task_input.grid(row=0, column=0, pady=10, padx=30)
add_button.grid(row=0, column=1)

# Load tasks from the file when the app starts
load_tasks()

# Root for the app
root.mainloop()
