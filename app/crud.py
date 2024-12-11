from fastapi import HTTPException
from app import models, database
from app.schemas import WishCreate, WishUpdate
from app.models import WishStatus

def get_all_wishes():
    db = database.SessionLocal()
    wishes = db.query(models.Wish).all()
    db.close()
    print(wishes)
    return wishes

def create_wish(wish: WishCreate):
    db = database.SessionLocal()
    try:
        existing_wish = db.query(models.Wish).filter_by(title=wish.title).first()
        if existing_wish:
            raise HTTPException(status_code=400, detail="Wish with the same name already exists.")

        new_wish = models.Wish(**wish.dict())
        db.add(new_wish)
        db.commit()
        db.refresh(new_wish)

        print(f"New wish created: {new_wish.title}")

        return new_wish

    except Exception as e:
        db.rollback()
        raise e

    finally:
        db.close()

def update_wish(wish_id: int, wish: WishUpdate):
    if not isinstance(wish_id, int):
        raise HTTPException(status_code=400, detail="Invalid wish_id, must be an integer.")

    db = database.SessionLocal()
    db_wish = db.query(models.Wish).get(wish_id)

    if not db_wish:
        raise HTTPException(status_code=404, detail="Wish not found")

    if wish.status not in WishStatus:
        raise HTTPException(status_code=400,
                            detail=f"Invalid status, allowed values are: {', '.join([status.value for status in WishStatus])}")

    if db_wish:
        for key, value in wish.dict().items():
            setattr(db_wish, key, value)
        db.commit()
        db.refresh(db_wish)

    db.close()
    return db_wish

def delete_wish(wish_id: int):
    if not isinstance(wish_id, int):
        raise HTTPException(status_code=400, detail="Invalid wish_id, must be an integer.")

    db = database.SessionLocal()
    db_wish = db.query(models.Wish).get(wish_id)

    if not db_wish:
        raise HTTPException(status_code=404, detail="Wish not found")

    if db_wish:
        db.delete(db_wish)
        db.commit()
    db.close()
    return {"message": "Wish deleted"}
