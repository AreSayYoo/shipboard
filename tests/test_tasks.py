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