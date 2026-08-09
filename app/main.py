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
    return{"tasks":project_tasks,
           "count": len(project_tasks)}

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