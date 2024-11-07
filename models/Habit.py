from db import get_db
from typing import List
from models import Base 
from models import User 
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

db = get_db()

class Habit(Base):
    __tablename__ = "habits"
    id : Mapped[int] = mapped_column(primary_key=True)
    habit : Mapped[str] = mapped_column(unique=True)
    desc : Mapped[str] = mapped_column()
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"))

    completions : Mapped[List["Track"]] = relationship(back_populates = "habit_completions",cascade="all, delete-orphan")
    user : Mapped["User"] = relationship(back_populates="habits")

class Track(Base):
    __tablename__ = "tracking"    
    id : Mapped[int] = mapped_column(primary_key=True)
    habit_id : Mapped[int] = mapped_column(ForeignKey("habits.id"),nullable=False)
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"),nullable=False)
    date : Mapped[datetime] = mapped_column(default=datetime.utcnow) 

    habit: Mapped["Habit"] = relationship(back_populates="completions")
