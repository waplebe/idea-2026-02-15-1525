# Simple CLI Todo List

This is a very basic command-line tool for managing a todo list.

## Usage

To add tasks, run the script with the task(s) as arguments:

```bash
python main.py task1 task2 task3
```

This will print the list of tasks to the console.

**Available Commands:**

*   `add`: Adds a task to the list.
*   `list`: Lists all tasks.
*   `remove <task_number>`: Removes a task by its number (starting from 1).

**Example:**

```bash
python main.py add "Buy groceries"
python main.py add "Walk the dog"
python main.py list
python main.py remove 1
python main.py list
```

## Features

*   **Task Persistence:** Tasks are saved to a JSON file (`todo.json`) and loaded when the application starts.
*   **Command-Line Interface:**  Provides a simple command-line interface for adding, listing, and removing tasks.
*   **Error Handling:** Includes basic error handling for invalid input (e.g., missing tasks, invalid task numbers).

## Bugs Fixed

*   Fixed an issue where the application would crash if the `todo.json` file was corrupted.
*   Fixed an issue where the application would not save tasks if they were added.
*   Fixed an issue where the application would not list tasks if the list was empty.

## Tests

Comprehensive unit tests have been added to ensure the functionality of the application.  The tests cover adding, listing, and removing tasks, as well as handling invalid input.

## Improvements

*   Added a `todo.json` file to persist tasks between sessions.
*   Implemented command-line arguments for adding, listing, and removing tasks.
*   Added error handling for invalid input.
*   Added unit tests to ensure the functionality of the application.