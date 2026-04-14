
import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task.strip() != "":
        tasks.append(task)
        listbox.insert(tk.END, "📝 " + task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
    except:
        messagebox.showwarning("Warning", "Select a task!")

def mark_done():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)
        listbox.delete(selected)
        listbox.insert(selected, "✔️ " + task)
    except:
        messagebox.showwarning("Warning", "Select a task!")

def clear_tasks():
    listbox.delete(0, tk.END)
    tasks.clear()

# Main Window
root = tk.Tk()
root.title("✨ To-Do List App")
root.geometry("350x500")
root.config(bg="#1e1e2f")

# Title
title = tk.Label(root, text="To-Do List", font=("Arial", 18, "bold"), bg="#1e1e2f", fg="white")
title.pack(pady=10)

# Entry Box
entry = tk.Entry(root, width=25, font=("Arial", 12))
entry.pack(pady=10)

# Buttons Frame
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack()

btn_add = tk.Button(frame, text="Add", width=10, bg="#4CAF50", fg="white", command=add_task)
btn_add.grid(row=0, column=0, padx=5, pady=5)

btn_delete = tk.Button(frame, text="Delete", width=10, bg="#f44336", fg="white", command=delete_task)
btn_delete.grid(row=0, column=1, padx=5, pady=5)

btn_done = tk.Button(frame, text="Done", width=10, bg="#2196F3", fg="white", command=mark_done)
btn_done.grid(row=1, column=0, padx=5, pady=5)

btn_clear = tk.Button(frame, text="Clear All", width=10, bg="#9C27B0", fg="white", command=clear_tasks)
btn_clear.grid(row=1, column=1, padx=5, pady=5)

# Listbox
listbox = tk.Listbox(root, width=30, height=15, font=("Arial", 12))
listbox.pack(pady=15)

root.mainloop()