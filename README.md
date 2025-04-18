# To-Do List Manager (Python CLI App)

This is a simple command-line To-Do List application written in Python that allows users to manage tasks efficiently. The tasks are saved to a file, so your list persists even after closing the program.

## Features

- **Add Tasks**: Input and save new tasks.
- **View Tasks**: Display the current list of tasks with numbering.
- **Remove Tasks**: Delete any task by selecting its number.
- **Persistent Storage**: Tasks are saved in a `tasks.txt` file for future sessions.
- **User-Friendly Interface**: Clear menu with input-based navigation.

## How It Works

1. **Load Tasks**: When you run the program, it loads tasks from `tasks.txt` if the file exists. If not, it creates a new empty list.
2. **Add Tasks**: You can add a new task by selecting option `1` and entering the task description.
3. **View Tasks**: You can view all your tasks with their corresponding numbers by selecting option `2`.
4. **Remove Tasks**: To remove a task, select option `3` and input the number of the task you want to delete.
5. **Exit**: Select option `4` to exit the program.
