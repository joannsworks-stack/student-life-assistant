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


print("=== 🎓 Student Life Assistant ===")

print(f"Date: {date_string}")

while True:

    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Daily Summary")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        task_name = input("Task name: ")

        priority = input(
            "Priority (High/Medium/Low): "
        ).capitalize()

        duration = input(
            "Estimated minutes: "
        )

        task = {
            "name": task_name,
            "priority": priority,
            "duration": duration,
            "completed": False
        }

        tasks.append(task)

        save_tasks()

        print("Task added!")

    elif choice == "2":

        if len(tasks) == 0:

            print("No tasks yet.")

        else:

            print("\n=== Today's Tasks ===")

            for i, task in enumerate(
                tasks,
                start=1
            ):

                status = (
                    "✅"
                    if task["completed"]
                    else "⬜"
                )

                print(
                    f"{i}. {status} "
                    f"{task['name']} | "
                    f"Priority: "
                    f"{task['priority']} | "
                    f"{task['duration']} mins"
                )

    elif choice == "3":

        if len(tasks) == 0:

            print("No tasks available.")

        else:

            task_num = int(
                input(
                    "Enter task number to complete: "
                )
            )

            if 1 <= task_num <= len(tasks):

                tasks[
                    task_num - 1
                ]["completed"] = True

                save_tasks()

                print(
                    "Task completed! ✅"
                )

            else:

                print(
                    "Invalid task number."
                )

    elif choice == "4":

        total_tasks = len(tasks)

        completed_tasks = 0

        total_minutes = 0

        pending_tasks = 0

        high_pending = False

        for task in tasks:

            total_minutes += int(
                task["duration"]
            )

            if task["completed"]:

                completed_tasks += 1

            else:

                pending_tasks += 1

                if (
                    task["priority"]
                    == "High"
                ):

                    high_pending = True

        if total_tasks == 0:

            productivity = 0

        else:

            productivity = round(
                (
                    completed_tasks
                    / total_tasks
                )
                * 100
            )

        print(
            "\n=== Daily Summary ==="
        )

        print(
            f"Total Tasks: {total_tasks}"
        )

        print(
            f"Completed: "
            f"{completed_tasks}"
        )

        print(
            f"Pending: "
            f"{pending_tasks}"
        )

        print(
            f"Total Study Time: "
            f"{total_minutes} mins"
        )

        print(
            f"Productivity Score: "
            f"{productivity}%"
        )

        print("\nSuggestion:")

        if high_pending:

            print(
                "Finish your High priority tasks first."
            )

        elif pending_tasks > 0:

            print(
                "You're doing well. Complete the remaining tasks."
            )

        else:

            print(
                "Excellent! All tasks are completed. 🎉"
            )

    elif choice == "5":

        if len(tasks) == 0:

            print("No tasks available.")

        else:

            print("\n=== Delete Task ===")

            for i, task in enumerate(
                tasks,
                start=1
            ):

                print(
                    f"{i}. {task['name']}"
                )

            task_num = int(
                input(
                    "Enter task number to delete: "
                )
            )

            if 1 <= task_num <= len(tasks):

                deleted = tasks.pop(
                    task_num - 1
                )

                save_tasks()

                print(
                    f"{deleted['name']} deleted 🗑️"
                )

            else:

                print(
                    "Invalid task number."
                )

    elif choice == "6":

        print("Goodbye!")

        break

    else:

        print("Invalid choice.")