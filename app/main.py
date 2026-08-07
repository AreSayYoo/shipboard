from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Shipboard")

class Project(BaseModel):
    id: int
    name: str
    status: str

projects = [
    Project(id= 1, name= "Learn Python", status= "ongoing"),
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