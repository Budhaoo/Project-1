import os

# File to store tasks
TASKS_FILE = "tasks.txt"

# Function to load tasks from the file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return [task.strip() for task in file.readlines()]
    return []

# Function to save tasks to the file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Main program
def todo_list():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added!")

        elif choice == "2":
            if not tasks:
                print("No tasks available.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    task_num = int(input("Enter the task number to remove: "))
                    if 1 <= task_num <= len(tasks):
                        removed_task = tasks.pop(task_num - 1)
                        save_tasks(tasks)
                        print(f"Removed: {removed_task}")
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            print("Exiting... Have a productive day!")
            break

        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")

# Run the app
todo_list()
