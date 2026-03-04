import argparse
import json
import os

DATA_FILE = "todo.json"

def load_tasks():
    """Loads tasks from the data file."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    else:
        return []

def save_tasks(tasks):
    """Saves tasks to the data file."""
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(task):
    """Adds a task to the list."""
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def list_tasks():
    """Lists all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

def remove_task(task_number):
    """Removes a task by its number."""
    tasks = load_tasks()
    try:
        index = int(task_number) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid task number. Please enter a number.")

def mark_complete(task_number):
    """Marks a task as complete."""
    tasks = load_tasks()
    try:
        index = int(task_number) - 1
        if 0 <= index < len(tasks):
            tasks[index] = f"[DONE] {tasks[index]}"
            save_tasks(tasks)
            print(f"Task '{tasks[index]}' marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid task number. Please enter a number.")

def prioritize_task(task_number, priority):
    """Prioritizes a task."""
    tasks = load_tasks()
    try:
        index = int(task_number) - 1
        if 0 <= index < len(tasks):
            tasks[index] = f"* {tasks[index]}"  # Add asterisk for priority
            save_tasks(tasks)
            print(f"Task '{tasks[index]}' prioritized.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid task number. Please enter a number.")

def main():
    parser = argparse.ArgumentParser(description="A simple command-line todo list.")
    parser.add_argument("action", choices=["add", "list", "remove", "complete", "prioritize"], help="Action to perform.")
    parser.add_argument("task", nargs="*", help="Task(s) to add or number of task to remove.")

    args = parser.parse_args()

    if args.action == "add":
        if not args.task:
            print("Please provide a task to add.")
        else:
            add_task(" ".join(args.task))
    elif args.action == "list":
        list_tasks()
    elif args.action == "remove":
        if not args.task:
            print("Please provide a task number to remove.")
        else:
            remove_task(args.task[0])
    elif args.action == "complete":
        if not args.task:
            print("Please provide a task number to mark as complete.")
        else:
            mark_complete(args.task[0])
    elif args.action == "prioritize":
        if not args.task or len(args.task) != 2:
            print("Usage: prioritize <task_number> <priority (e.g., high, medium, low)>")
            return
        try:
            task_number = args.task[0]
            priority = args.task[1].lower()
            prioritize_task(task_number, priority)
        except ValueError:
            print("Invalid priority. Please use 'high', 'medium', or 'low'.")


if __name__ == "__main__":
    main()