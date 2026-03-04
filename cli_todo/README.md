# Simple CLI Todo List

This is a command-line tool for managing a todo list.

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

To mark a task as complete, run:

```bash
python main.py complete 1
```

This will mark the task at index 1 as complete.

To prioritize a task, run:

```bash
python main.py prioritize 1 high
```

This will set the priority of the task at index 1 to high.

## Commands

*   `add <task(s)>`: Adds one or more tasks to the list. Tasks are joined with spaces.
*   `list`: Lists all tasks.
*   `remove <task_number>`: Removes a task by its number (starting from 1).
*   `complete <task_number>`: Marks a task as complete.
*   `prioritize <task_number> <priority>`: Prioritizes a task. Priority can be 'high', 'medium', or 'low'.

## Features

*   **Task Persistence:** Tasks are saved to a JSON file (`todo.json`) and loaded when the application starts.
*   **Command-Line Interface:** Provides a simple command-line interface for adding, listing, removing, marking tasks as complete, and prioritizing tasks.
*   **Error Handling:** Includes basic error handling for invalid input (e.g., missing tasks, invalid task numbers).

## Bugs Fixed

*   Fixed an issue where the application would crash if the `todo.json` file was corrupted.
*   Fixed an issue where the application would not save tasks if they were added.
*   Fixed an issue where the application would not list tasks if the list was empty.
*   Added tests to ensure task persistence.
*   Added functionality to mark tasks as complete.
*   Added functionality to prioritize tasks.

## Tests

Comprehensive unit tests have been added to ensure the functionality of the application. The tests cover adding, listing, removing tasks, handling invalid input, and verifying task persistence, as well as the new "complete" and "prioritize" functionality.

## Improvements

*   **Task Persistence:** Implemented task persistence using a JSON file.
*   **Command-Line Arguments:** Improved command-line argument parsing for clarity and flexibility.
*   **Error Handling:** Enhanced error handling for invalid input.
*   **Unit Tests:** Added comprehensive unit tests to ensure the application's reliability.
*   **Documentation:** Updated the README with clear usage instructions and a description of the features.
*   **Example Usage:** Added example commands to the README.
*   **New Features:** Implemented the ability to mark tasks as complete and prioritize tasks.

## Future Enhancements

*   **Priority Levels:** Add support for assigning priority levels to tasks.
*   **Due Dates:** Allow users to set due dates for tasks.
*   **Filtering:** Implement filtering options to view tasks based on criteria (e.g., priority, due date).
*   **GUI:** Consider developing a graphical user interface for the todo list.

## Prioritization Details

Tasks can be prioritized using the `prioritize` command.  The priority can be set to `high`, `medium`, or `low`.  The task at the specified number will have its priority marked with an asterisk (*) at the beginning of the task description.

## Example

```bash
python main.py prioritize 1 high
```

This will mark the first task in the list as high priority.