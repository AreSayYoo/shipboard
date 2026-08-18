from fastapi import HTTPException
from app.data import projects, tasks
from app.models import Project, Task

def find_project(project_id: int) -> Project:
    for project in projects:
        if project.id == project_id:
            return project
    raise HTTPException(status_code=404, detail="Project not found")

def find_task(task_id: int) -> Task:
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

def get_task_index(task_id: int) -> int:
    for i, task in enumerate(tasks):
        if task.id == task_id:
            return i
    raise HTTPException(status_code=404, detail="Task not found")