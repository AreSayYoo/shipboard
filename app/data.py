from app.models import Project, Task

projects = [
    Project(id= 1, name= "Learn Python", status= "ongoing"),
]

tasks = [
    Task(id=1, project_id=1, title="Download Python", completed=True)
]