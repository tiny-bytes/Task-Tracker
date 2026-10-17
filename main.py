"""Command-line entry point for the Task Tracker demo."""

import argparse
from task_tracker.storage import load_tasks, save_tasks
from task_tracker.tasks import add_task, complete_task, delete_task, list_tasks


def main():
    parser = argparse.ArgumentParser(description="A simple command-line task tracker.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("list", help="List all tasks")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Task description")

    done_parser = subparsers.add_parser("done", help="Mark a task complete")
    done_parser.add_argument("task_id", type=int, help="ID of the task")

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("task_id", type=int, help="ID of the task")

    args = parser.parse_args()
    tasks = load_tasks()

    if args.command == "list":
        list_tasks(tasks)
    elif args.command == "add":
        add_task(tasks, args.description)
        save_tasks(tasks)
        print("Task added.")
    elif args.command == "done":
        if complete_task(tasks, args.task_id):
            save_tasks(tasks)
            print(f"Task {args.task_id} marked complete.")
        else:
            print(f"Task {args.task_id} not found.")
    elif args.command == "delete":
        if delete_task(tasks, args.task_id):
            save_tasks(tasks)
            print(f"Task {args.task_id} deleted.")
        else:
            print(f"Task {args.task_id} not found.")


if __name__ == "__main__":
    main()
