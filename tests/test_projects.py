from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home_page():
    response = client.get("/")
    assert response.status_code == 200

def test_get_projects():
    response = client.get("/projects")
    assert response.status_code == 200
    assert "projects","count" in response

def test_get_project_1():
    response = client.get("/projects/1")
    assert response.status_code == 200

def test_get_invalid_project():
    response = client.get("projects/999")
    assert response.status_code == 404