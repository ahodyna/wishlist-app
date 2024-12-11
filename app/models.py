from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from app.schemas import WishStatus
from datetime import datetime

Base = declarative_base()

class Wish(Base):
    __tablename__ = "wishes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(Enum(WishStatus), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    priority = Column(Integer, nullable=False)
    category = Column(String)

    @classmethod
    def filter_by_category(cls, query, category):
        if category:
            query = query.filter(cls.category == category)
        return query