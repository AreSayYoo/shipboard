from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_tasks():
    response = client.get("/projects/1/tasks")
    assert response.status_code == 200

    data = response.json() 
    assert "tasks" in data
    assert "count" in data
