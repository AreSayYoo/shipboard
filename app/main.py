from fastapi import FastAPI

app = FastAPI(title="Shipboard")

@app.get("/")
def home():
    return {"message": "Shipboard is running"}

@app.get("/about")
def about():
    return {"name": "Shipboard",
            "description": "To-do list app created by Matt Arceo.",
            "purpose": "Designed to help keep my work in order and not miss anything important coming from all directions."}