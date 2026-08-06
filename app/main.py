from fastapi import FastAPI

app = FastAPI(title="Shipboard")

@app.get("/")
def home():
    return{"message": "Shipboard is running"}