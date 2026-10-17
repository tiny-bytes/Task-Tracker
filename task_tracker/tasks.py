"""Task operations and display helpers."""


def add_task(tasks, description):
    description = description.strip()
    if not description:
        raise ValueError("Task description cannot be empty.")
    next_id = max((task["id"] for task in tasks), default=0) + 1
    tasks.append({"id": next_id, "description": description, "completed": False})


def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return True
    return False


def delete_task(tasks, task_id):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[index]
            return True
    return False


def list_tasks(tasks):
    if not tasks:
        print("No tasks yet. Add one with: python main.py add \"Your task\"")
        return
    for task in tasks:
        status = "x" if task["completed"] else " "
        print(f'[{status}] {task["id"]}. {task["description"]}')
