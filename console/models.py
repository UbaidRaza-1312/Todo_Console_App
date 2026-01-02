from typing import Optional
from datetime import datetime

class Task:
    def __init__(self, id: int, title: str, description: Optional[str] = None, status: bool = False, created_at: Optional[datetime] = None):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("Task ID must be a positive integer.")
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Task title cannot be empty.")
        if description is not None and not isinstance(description, str):
            raise ValueError("Task description must be a string or None.")
        if not isinstance(status, bool):
            raise ValueError("Task status must be a boolean.")

        self.id: int = id
        self.title: str = title
        self.description: Optional[str] = description
        self.status: bool = status
        self.created_at: datetime = created_at or datetime.now()

    def __repr__(self) -> str:
        return (f"Task(id={self.id}, title='{self.title}', "
                f"description='{self.description}', status={self.status}, "
                f"created_at='{self.created_at.isoformat()}')")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.isoformat()
        }

    @staticmethod
    def from_dict(data: dict) -> 'Task':
        return Task(
            id=data['id'],
            title=data['title'],
            description=data.get('description'),
            status=data.get('status', False),
            created_at=datetime.fromisoformat(data['created_at']) if 'created_at' in data else None
        )
