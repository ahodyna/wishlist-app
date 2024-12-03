from pydantic import BaseModel

class WishBase(BaseModel):
    title: str
    description: str

class WishCreate(WishBase):
    pass

class WishUpdate(WishBase):
    pass

class Wish(WishBase):
    id: int

    class Config:
        orm_mode = True
