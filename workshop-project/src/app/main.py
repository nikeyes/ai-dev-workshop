from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title='Tasks API')


tasks: dict[int, dict] = {}
_next_id = 1


class TaskCreate(BaseModel):
    title: str
    done: bool = False


class Task(BaseModel):
    id: int
    title: str
    done: bool


@app.get('/tasks', response_model=list[Task])
def list_tasks():
    return list(tasks.values())


@app.post('/tasks', response_model=Task, status_code=201)
def create_task(body: TaskCreate):
    global _next_id
    task = {'id': _next_id, 'title': body.title, 'done': body.done}
    tasks[_next_id] = task
    _next_id += 1
    return task


@app.get('/tasks/{task_id}', response_model=Task)
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail='Task not found')
    return tasks[task_id]


@app.delete('/tasks/{task_id}', status_code=204)
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail='Task not found')
    del tasks[task_id]
