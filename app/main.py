from fastapi import FastAPI
from app.models import Project, ProjectCreate, Task, TaskCreate
from app.data import projects, tasks
from app.services import find_project, find_task, get_task_index

app = FastAPI(title="Shipboard")

@app.get("/")
def home():
    return {"message": "Shipboard is running"}

@app.get("/about")
def about():
    return {"name": "Shipboard",
            "description": "To-do list app created by Matt Arceo.",
            "purpose": "Designed to help keep my work in order and not miss anything important coming from all directions."}

@app.get("/projects")
def get_projects():
    count = len(projects)
    return {"projects": projects,
            "count": count}

@app.get("/projects/{project_id}")
def get_project_id(project_id: int) -> Project:
    return find_project(project_id)

@app.get("/projects/{project_id}/tasks")
def get_tasks_for_project(project_id: int):
    project_tasks = []
    for task in tasks:
        if task.project_id == project_id:
            project_tasks.append(task)
    return{
        "tasks":project_tasks,
        "count": len(project_tasks),
        }

@app.post("/projects")
def add_project(project_data: ProjectCreate):
    next_id = len(projects) + 1
    project = Project(
        id=next_id,
        name=project_data.name,
        status=project_data.status
    )
    projects.append(project)
    return project

@app.post("/projects/{project_id}/tasks")
def add_task(project_id: int, task_data: TaskCreate) -> Task:
    project = find_project(project_id)
    next_id = len(tasks) + 1
    task = Task(
        id=next_id,
        project_id=project.id,
        title=task_data.title,
        completed=task_data.completed
    )
    tasks.append(task)
    return task


@app.patch("/tasks/{task_id}/complete")
def complete_task(task_id: int) -> Task:
    task = find_task(task_id)
    task.completed = True
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    task_index = get_task_index(task_id)
    deleted_task = tasks.pop(task_index)
    return{
        "message": "Task deleted.",
        "task": deleted_task,
    }
