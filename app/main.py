from fastapi import FastAPI

from app.database import Base, engine
from app.models.item import Item

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Found-X")


@app.get("/")
def home():
    return {
        "message": "Welcome to Found-X"
    }