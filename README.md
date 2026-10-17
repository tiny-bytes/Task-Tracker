# Task Tracker

A small Python command-line task tracker for demonstrating Git and GitHub workflows.

## Requirements
- Python 3.9 or newer
- No third-party packages required

## Run
From this folder:

```bash
python main.py list
python main.py add "Prepare Git presentation"
python main.py list
python main.py done 1
python main.py list
```

On Windows, use `py main.py ...` if `python` is not recognized.

## Commands
- `list` — show all tasks
- `add "task description"` — add a task
- `done TASK_ID` — mark a task complete
- `delete TASK_ID` — delete a task

Tasks are saved in `tasks.json`.

## Git live-demo ideas
1. Edit `README.md` and commit the change.
2. Create a feature branch and add a small feature.
3. Merge the feature branch into `main`.
4. Use `git log --oneline --graph --all` to inspect history.
5. Demonstrate `git revert` or `git reset --soft` only on a practice branch.
