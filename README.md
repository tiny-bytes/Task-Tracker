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


## Contribution Notes

Contributions to the Task Tracker project are welcome. Follow these steps to contribute:

1. Clone the repository to your local machine.
2. Pull the latest changes from the `main` branch.
3. Make the required changes to the project.
4. Test your changes before committing.
5. Stage and commit your changes with a clear commit message.
6. Push your changes to GitHub.

### Git Commands

```bash
git clone <repository-url>
git pull origin main
git add .
git commit -m "Describe your changes"
git push origin main
```

**Note:** Ensure your changes do not break existing functionality before pushing them.
