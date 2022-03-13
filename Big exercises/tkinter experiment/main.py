from tkinter.ttk import *
from tkinter import *
from tkcalendar import DateEntry
from tkinter.scrolledtext import *


def create_task(*args):
    print(args)


def render_create_task_view(window):
    for s in window.grid_slaves():
        s.destroy()
    Label(window, text="Enter your task name: ").grid(row=0, column=0, padx=20, pady=20)
    task_name = Entry(window)
    task_name.grid(row=0, column=1, padx=20, pady=20)
    Label(window, text="Due date: ").grid(row=1, column=0, padx=20, pady=20)
    date = DateEntry(window)
    date.grid(row=1, column=1)
    description = ScrolledText(window, width=40, height=15)
    description.grid(row=2, column=1, padx=20, pady=20)
    Label(window, text="Select priority: ").grid(row=3, column=0, padx=20, pady=20)
    selected_priority_num = IntVar()
    Radiobutton(window, text="malko", value=1, variable=selected_priority_num).grid(row=3, column=1, padx=20, pady=20)
    Radiobutton(window, text="sredno", value=2, variable=selected_priority_num).grid(row=3, column=2, padx=20, pady=20)
    Radiobutton(window, text="mnogo", value=3, variable=selected_priority_num).grid(row=3, column=3, padx=20, pady=20)
    Label(window, text="Boli li te guza? ").grid(row=4, column=0, padx=20, pady=20)
    Checkbutton(window, text="Da").grid(row=4, column=1, padx=20, pady=20)
    Checkbutton(window, text="Ne").grid(row=4, column=2, padx=20, pady=20)
    Button(window, text="Gotovo", bg="green", fg="red", command=lambda: create_task(task_name.get(), date.get(), description.get("1.0", END), selected_priority_num.get())).grid(row=5, column=0, padx=20, pady=80)

def render_main_view(tk):
    Button(window, text="Baba ti", bg="green", fg="red", command=lambda: render_create_task_view(window)).grid(row=2, column=3, padx=20, pady=20)
    Button(window, text="Runtav guz", bg="green", fg="red").grid(row=3, column=4, padx=20, pady=20)


window = Tk()
window.geometry("800x900")
render_main_view(window)
window.mainloop()
