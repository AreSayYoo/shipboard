from pydantic import BaseModel

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