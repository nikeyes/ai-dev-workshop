import pytest
from fastapi.testclient import TestClient

import app.main as main_module
from app.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_state():
    main_module.tasks.clear()
    main_module._next_id = 1


def test_summarize_tasks_counts_total():
    from app.main import summarize_tasks

    task_list = [
        {'id': 1, 'title': 'Done task', 'done': True},
        {'id': 2, 'title': 'Pending task', 'done': False},
        {'id': 3, 'title': 'Another pending', 'done': False},
    ]

    result = summarize_tasks(task_list)

    assert result['total'] == 3


def test_list_tasks_returns_empty_list_initially():
    response = client.get('/tasks')
    assert response.status_code == 200
    assert response.json() == []


def test_create_task_returns_created_task():
    response = client.post('/tasks', json={'title': 'Buy milk'})
    assert response.status_code == 201
    data = response.json()
    assert data['title'] == 'Buy milk'
    assert data['done'] is False
    assert data['id'] == 1


def test_list_tasks_returns_created_tasks():
    client.post('/tasks', json={'title': 'Task A'})
    client.post('/tasks', json={'title': 'Task B'})

    response = client.get('/tasks')
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_task_returns_task():
    client.post('/tasks', json={'title': 'My task'})

    response = client.get('/tasks/1')
    assert response.status_code == 200
    assert response.json()['title'] == 'My task'


def test_get_task_returns_404_when_not_found():
    response = client.get('/tasks/999')
    assert response.status_code == 404


def test_delete_task_removes_it():
    client.post('/tasks', json={'title': 'To delete'})

    client.delete('/tasks/1')

    assert client.get('/tasks/1').status_code == 404


def test_delete_task_returns_404_when_not_found():
    response = client.delete('/tasks/999')
    assert response.status_code == 404
