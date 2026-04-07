# from app.service import tasks  # noqa: F401
from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    done: bool = False


class Task(BaseModel):
    id: int
    title: str
    done: bool
