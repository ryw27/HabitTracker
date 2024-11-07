from db import get_db
from typing import List
from models import Habit 
from models import Base 
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login  


db = get_db()

class User(UserMixin,Base):
    __tablename__ = "users" 
    id : Mapped[int] = mapped_column(primary_key=True)
    username : Mapped[str]= mapped_column(String(50),unique=True)
    email : Mapped[str] = mapped_column(String(100),unique=True)
    password : Mapped[str] = mapped_column(String(255))
    habits : Mapped[List["Habit"]] = relationship(back_populates="user")
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

#user loader, unique identifier keep track of logged in
@login.user_loader
def load_user(id):
    return db.session.get(User,int(id))