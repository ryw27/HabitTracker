from db import get_db
from datetime import datetime
from typing import List
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = get_db()
Base = declarative_base()
class User(Base):
    __tablename__ = "users" 
    id : Mapped[int] = mapped_column(primary_key=True)
    username : Mapped[str]= mapped_column(String(50),unique=True)
    email : Mapped[str] = mapped_column(String(100),unique=True)
    password : Mapped[str] = mapped_column(String(255))
    habits : Mapped[List["User"]] = relationship("Habit",back_populates="user")
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
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

    habit_completions : Mapped["Habit"] = relationship(back_populates="completions")

# @login.user_loader
# def load_user(id):
#     return db.session.get(User,int(id))