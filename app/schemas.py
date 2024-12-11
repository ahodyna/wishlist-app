from pydantic import BaseModel
from enum import Enum

class WishStatus(str, Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

class WishBase(BaseModel):
    title: str
    description: str
    status: WishStatus

class WishCreate(WishBase):
    pass

class WishUpdate(WishBase):
    pass

class Wish(WishBase):
    id: int

    class Config:
        orm_mode = True
