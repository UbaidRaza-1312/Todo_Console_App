import json
from typing import Dict, Optional
from console.models import Task

class TaskService:
    def __init__(self, file_path: str = "tasks.json"):
        self._file_path = file_path
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1
        self._load_tasks()

    def _load_tasks(self):
        try:
            with open(self._file_path, 'r') as f:
                tasks_data = json.load(f)
                for task_data in tasks_data:
                    task = Task.from_dict(task_data)
                    self._tasks[task.id] = task
                if self._tasks:
                    self._next_id = max(self._tasks.keys()) + 1
        except (FileNotFoundError, json.JSONDecodeError):
            self._tasks = {}
            self._next_id = 1

    def _save_tasks(self):
        with open(self._file_path, 'w') as f:
            json.dump([task.to_dict() for task in self._tasks.values()], f, indent=4)

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty.")

        task = Task(id=self._next_id, title=title, description=description)
        self._tasks[self._next_id] = task
        self._next_id += 1
        self._save_tasks()
        return task

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        return self._tasks.get(task_id)

    def get_all_tasks(self) -> list[Task]:
        return list(self._tasks.values())

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None, status: Optional[bool] = None) -> Task:
        task = self._tasks.get(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found.")

        if title is not None:
            if not title.strip():
                raise ValueError("Task title cannot be empty.")
            task.title = title
        if description is not None:
            task.description = description
        if status is not None:
            task.status = status
        
        self._save_tasks()
        return task

    def delete_task(self, task_id: int) -> None:
        if task_id not in self._tasks:
            raise ValueError(f"Task with ID {task_id} not found.")
        del self._tasks[task_id]
        self._save_tasks()

    def clear_tasks(self) -> None:
        self._tasks = {}
        self._next_id = 1
        self._save_tasks()

    def mark_task_as_done(self, task_id: int) -> Task:
        return self.update_task(task_id, status=True)