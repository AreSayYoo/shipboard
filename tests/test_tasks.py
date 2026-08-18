from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_tasks():
    response = client.get("/projects/1/tasks")
    assert response.status_code == 200

    data = response.json() 
    assert "tasks" in data
    assert "count" in data

def test_add_task():
    response = client.post(
        "/projects/1/tasks",
        json={
            "title": "Learn Syntax"
        },
    )
    assert response.status_code == 200

    data = response.json()
    assert "id" in data
    assert data["project_id"] == 1
    assert data["title"] == "Learn Syntax"
    assert data["completed"] is False

def test_complete_task():
    create_response = client.post(
        "/projects/1/tasks",
        json={"title": "Complete me!!"},
    )

    created_task = create_response.json()
    task_id = created_task["id"]

    response = client.patch(f"/tasks/{task_id}/complete")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == task_id
    assert data["completed"] is True

def test_delete_task():
    create_response = client.post(
        "/projects/1/tasks",
        json={"title": "Delete me!!"},
    )

    created_task = create_response.json()
    task_id = created_task["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200

    data = response.json()
    assert data["message"] == "Task deleted."
    assert data["task"]["id"] == task_id

    delete_response_again = client.delete(f"/tasks/{task_id}")
    assert delete_response_again.status_code == 404

def test_create_invalid_task():
    create_response = client.post(
        "/projects/999/tasks",
        json={"title": "This should not work..."}
    )

    assert create_response.status_code == 404

    data = create_response.json()
    assert data["detail"] == "Project not found"
