from sqlalchemy.orm import Session
from app import models, database
from app.schemas import WishCreate, WishUpdate

def get_all_wishes():
    db = database.SessionLocal()
    wishes = db.query(models.Wish).all()
    db.close()
    print(wishes)
    return wishes

def create_wish(wish: WishCreate):
    db = database.SessionLocal()
    new_wish = models.Wish(**wish.dict())
    db.add(new_wish)
    db.commit()
    db.refresh(new_wish)
    db.close()
    return new_wish

def update_wish(wish_id: int, wish: WishUpdate):
    db = database.SessionLocal()
    db_wish = db.query(models.Wish).get(wish_id)
    if db_wish:
        for key, value in wish.dict().items():
            setattr(db_wish, key, value)
        db.commit()
        db.refresh(db_wish)
    db.close()
    return db_wish

def delete_wish(wish_id: int):
    db = database.SessionLocal()
    db_wish = db.query(models.Wish).get(wish_id)
    if db_wish:
        db.delete(db_wish)
        db.commit()
    db.close()
    return {"message": "Wish deleted"}
