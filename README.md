# Simple CLI Todo List

This is a simple command-line tool for managing a todo list.  It persists tasks to a JSON file, allowing them to be carried over between sessions.

## Usage

To add tasks, run the script with the task(s) as arguments:

```bash
python main.py add "Buy groceries" "Walk the dog"
```

This will add both "Buy groceries" and "Walk the dog" to the todo list.

To list all tasks, run:

```bash
python main.py list
```

To remove a task by its number, run:

```bash
python main.py remove 1
```

This will remove the task at index 1 (remembering that task numbers start at 1).

## Commands

*   `add <task(s)>`: Adds one or more tasks to the list. Tasks are joined with spaces.
*   `list`: Lists all tasks.
*   `remove <task_number>`: Removes a task by its number (starting from 1).

## Features

*   **Task Persistence:** Tasks are saved to a JSON file (`todo.json`) and loaded when the application starts.
*   **Command-Line Interface:** Provides a simple command-line interface for adding, listing, and removing tasks.
*   **Error Handling:** Includes basic error handling for invalid input (e.g., missing tasks, invalid task numbers).

## Bugs Fixed

*   Fixed an issue where the application would crash if the `todo.json` file was corrupted.
*   Fixed an issue where the application would not save tasks if they were added.
*   Fixed an issue where the application would not list tasks if the list was empty.
*   Added tests to ensure task persistence.

## Tests

Comprehensive unit tests have been added to ensure the functionality of the application. The tests cover adding, listing, removing tasks, handling invalid input, and verifying task persistence.

## Improvements

*   **Task Persistence:** Implemented task persistence using a JSON file.
*   **Command-Line Arguments:**  Improved command-line argument parsing for clarity and flexibility.
*   **Error Handling:** Enhanced error handling for invalid input.
*   **Unit Tests:** Added comprehensive unit tests to ensure the application's reliability.
*   **Documentation:** Updated the README with clear usage instructions and a description of the features.
*   **Example Usage:** Added example commands to the README.

## Future Enhancements

*   **Priority Levels:** Add support for assigning priority levels to tasks.
*   **Due Dates:** Allow users to set due dates for tasks.
*   **Filtering:** Implement filtering options to view tasks based on criteria (e.g., priority, due date).
*   **GUI:** Consider developing a graphical user interface for the todo list.

---