tasks: dict[int, dict] = {}
_next_id = 1


def summarize_tasks(task_list: list[dict]) -> dict:
    total = len(task_list)
    done = len([t for t in task_list if t['done']])
    pending = total - done
    progress = (done * 100) // total if total > 0 else 0
    return {'total': total, 'done': done, 'pending': pending, 'progress': progress}


def list_all_tasks() -> list[dict]:
    return list(tasks.values())


def create_task(title: str, done: bool = False) -> dict:
    global _next_id
    task = {'id': _next_id, 'title': title, 'done': done}
    tasks[_next_id] = task
    _next_id += 1
    return task


def get_task(task_id: int) -> dict | None:
    return tasks.get(task_id)


def delete_task(task_id: int) -> bool:
    if task_id not in tasks:
        return False
    del tasks[task_id]
    return True
