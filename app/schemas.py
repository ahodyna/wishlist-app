from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class WishStatus(str, Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

class WishBase(BaseModel):
    title: str
    description: str
    status: WishStatus
    created_at: datetime
    priority: int
    category: str

class WishCreate(WishBase):
    pass

class WishUpdate(WishBase):
    pass

class Wish(WishBase):
    id: int

    class Config:
        orm_mode = True

class SortByEnum(str, Enum):
    created_at = "created_at"
    priority = "priority"
    status = "status"