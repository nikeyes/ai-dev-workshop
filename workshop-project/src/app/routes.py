from fastapi import APIRouter, HTTPException

from app.models import Task, TaskCreate
from app.service import create_task, delete_task, get_task, list_all_tasks

router = APIRouter()


@router.get('/tasks', response_model=list[Task])
def list_tasks():
    return list_all_tasks()


@router.post('/tasks', response_model=Task, status_code=201)
def create(body: TaskCreate):
    return create_task(title=body.title, done=body.done)


@router.get('/tasks/{task_id}', response_model=Task)
def get(task_id: int):
    task = get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail='Task not found')
    return task


@router.delete('/tasks/{task_id}', status_code=204)
def delete(task_id: int):
    if not delete_task(task_id):
        raise HTTPException(status_code=404, detail='Task not found')
