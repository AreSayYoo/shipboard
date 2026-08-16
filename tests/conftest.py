import pytest

from app.data import projects, tasks
from app.models import Project, Task

@pytest.fixture(autouse=True)
def reset_data():
    projects.clear()
    tasks.clear()

    projects.append(Project(
        id=1, 
        name="Learn Python",
        status="ongoing"
    ))

    tasks.append(Task(
        id=1,
        project_id=1,
        title="Download Python",
        completed=False
    ))