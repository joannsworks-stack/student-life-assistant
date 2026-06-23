import tkinter as tk
from tkinter import simpledialog
import json
import os
from datetime import datetime

today = datetime.now()

date_string = today.strftime("%d %B %Y")

file_name = f"{date_string}.json"

if os.path.exists(file_name):

    with open(file_name, "r") as file:

        tasks = json.load(file)

else:

    tasks = []


def save_tasks():

    with open(file_name, "w") as file:

        json.dump(tasks, file, indent=4)


def add_task():

    task_name = simpledialog.askstring(
        "Task",
        "Task name:"
    )

    if not task_name:

        return

    priority = simpledialog.askstring(
        "Priority",
        "High/Medium/Low:"
    )

    if not priority:

        return

    duration = simpledialog.askstring(
        "Duration",
        "Estimated minutes:"
    )

    if not duration:

        return

    task = {

        "name": task_name,

        "priority": priority.capitalize(),

        "duration": duration,

        "completed": False

    }

    tasks.append(task)

    save_tasks()

    status_label.config(
        text="Task Added ✅"
    )

    view_tasks()


def view_tasks():

    task_box.delete(
        "1.0",
        tk.END
    )

    if len(tasks) == 0:

        task_box.insert(
            tk.END,
            "No tasks yet."
        )

    else:

        for i, task in enumerate(
            tasks,
            start=1
        ):

            status = (
                "✅"
                if task["completed"]
                else "⬜"
            )

            task_box.insert(

                tk.END,

                f"{i}. "

                f"{status} "

                f"{task['name']} | "

                f"{task['priority']} | "

                f"{task['duration']} mins\n"

            )

    status_label.config(
        text="Tasks Loaded ✅"
    )


def complete_task():

    if len(tasks) == 0:

        return

    task_num = simpledialog.askinteger(
        "Complete Task",
        "Task number:"
    )

    if task_num:

        if 1 <= task_num <= len(tasks):

            tasks[task_num - 1][
                "completed"
            ] = True

            save_tasks()

            status_label.config(
                text="Task Completed ✅"
            )

            view_tasks()


def delete_task():

    if len(tasks) == 0:

        return

    task_num = simpledialog.askinteger(
        "Delete Task",
        "Task number:"
    )

    if task_num:

        if 1 <= task_num <= len(tasks):

            deleted = tasks.pop(
                task_num - 1
            )

            save_tasks()

            status_label.config(
                text=f"{deleted['name']} Deleted 🗑️"
            )

            view_tasks()


def summary():

    total = len(tasks)

    completed = 0

    pending = 0

    total_minutes = 0

    high_pending = False

    for task in tasks:

        total_minutes += int(
            task["duration"]
        )

        if task["completed"]:

            completed += 1

        else:

            pending += 1

            if task["priority"] == "High":

                high_pending = True

    if total == 0:

        productivity = 0

    else:

        productivity = round(
            (completed / total) * 100
        )

    task_box.delete(
        "1.0",
        tk.END
    )

    task_box.insert(

        tk.END,

        f"=== Daily Summary ===\n\n"

        f"Total Tasks: {total}\n"

        f"Completed: {completed}\n"

        f"Pending: {pending}\n"

        f"Study Time: {total_minutes} mins\n"

        f"Productivity: {productivity}%\n\n"

    )

    if high_pending:

        task_box.insert(

            tk.END,

            "Suggestion:\nFinish your High priority tasks first."

        )

    elif pending > 0:

        task_box.insert(

            tk.END,

            "Suggestion:\nComplete your remaining tasks."

        )

    else:

        task_box.insert(

            tk.END,

            "Suggestion:\nExcellent! 🎉"

        )

    status_label.config(
        text="Summary Loaded 📊"
    )


window = tk.Tk()

window.title(
    "🎓 Student Life Assistant"
)

window.geometry(
    "650x650"
)

window.resizable(
    False,
    False
)

window.configure(
    bg="#f5f5f5"
)


title = tk.Label(

    window,

    text="🎓 Student Life Assistant",

    font=("Arial", 20, "bold"),

    bg="#f5f5f5",

    fg="#1f4e79"

)

title.pack(
    pady=10
)


date_label = tk.Label(

    window,

    text=f"📅 {date_string}",

    font=("Arial", 12),

    bg="#f5f5f5"

)

date_label.pack()


task_box = tk.Text(

    window,

    height=15,

    width=55,

    font=("Arial", 11)

)

task_box.pack(
    pady=20
)


button_frame = tk.Frame(

    window,

    bg="#f5f5f5"

)

button_frame.pack()


tk.Button(

    button_frame,

    text="➕ Add",

    width=14,

    bg="#4CAF50",

    fg="white",

    command=add_task

).grid(row=0, column=0, padx=5, pady=5)


tk.Button(

    button_frame,

    text="📋 View",

    width=14,

    bg="#2196F3",

    fg="white",

    command=view_tasks

).grid(row=0, column=1, padx=5, pady=5)


tk.Button(

    button_frame,

    text="✅ Complete",

    width=14,

    bg="#FF9800",

    fg="white",

    command=complete_task

).grid(row=1, column=0, padx=5, pady=5)


tk.Button(

    button_frame,

    text="📊 Summary",

    width=14,

    bg="#9C27B0",

    fg="white",

    command=summary

).grid(row=1, column=1, padx=5, pady=5)


tk.Button(

    button_frame,

    text="🗑️ Delete",

    width=14,

    bg="#F44336",

    fg="white",

    command=delete_task

).grid(row=2, column=0, padx=5, pady=5)


tk.Button(

    button_frame,

    text="🚪 Exit",

    width=14,

    bg="#607D8B",

    fg="white",

    command=window.destroy

).grid(row=2, column=1, padx=5, pady=5)


status_label = tk.Label(

    window,

    text="Ready ✅",

    font=("Arial", 10),

    bg="#f5f5f5"

)

status_label.pack(
    pady=15
)


footer_label = tk.Label(

    window,

    text="© 2026 JOANNS WORKS | Student Life Assistant | Developed by George M Chacko",

    font=("Arial", 8),

    bg="#f5f5f5",

    fg="#666666"

)

footer_label.pack(
    pady=5
)


window.mainloop()