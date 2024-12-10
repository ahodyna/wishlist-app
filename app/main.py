from fastapi import FastAPI
from app import models, database, crud
from app.schemas import WishCreate, WishUpdate

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Wish List App"}

@app.get("/wishes/")
def get_wishes():
    return crud.get_all_wishes()

@app.post("/wishes/")
def create_wish(wish: WishCreate):
    return crud.create_wish(wish)

@app.put("/wishes/{wish_id}")
def update_wish(wish_id: int, wish: WishUpdate):
    return crud.update_wish(wish_id, wish)

@app.delete("/wishes/{wish_id}")
def delete_wish(wish_id: int):
    return crud.delete_wish(wish_id)
