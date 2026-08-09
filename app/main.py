from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Shipboard")

class Project(BaseModel):
    id: int
    name: str
    status: str

class ProjectCreate(BaseModel):
    name: str
    status: str

class Task(BaseModel):
    id: int
    project_id: int
    title: str
    completed: bool

class TaskCreate(BaseModel):
    title: str
    completed: bool = False

projects = [
    Project(id= 1, name= "Learn Python", status= "ongoing"),
]

tasks = [
    Task(id=1, project_id=1, title="Download Python", completed=True)
]

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
    for project in projects:
        if project.id == project_id:
            return project
    raise HTTPException(status_code=404, detail="Project not found")

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
    for project in projects:
        if project.id == project_id:
            next_id = len(tasks) + 1
            task = Task(
                id=next_id,
                project_id=project_id,
                title=task_data.title,
                completed=task_data.completed
            )
            tasks.append(task)
            return task
    raise HTTPException(status_code=404, detail="Project does not exist.")

@app.patch("/tasks/{task_id}/complete")
def complete_task(task_id: int) -> Task:
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            return task
    raise HTTPException(status_code=404,detail="Task not found.")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            deleted_task = tasks.pop(i)
            return{
                "message": "Task deleted.",
                "task": deleted_task,
            }
    raise HTTPException(status_code=404,detail="Task not found.")