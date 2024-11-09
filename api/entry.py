from flask import Blueprint, request, redirect, render_template
from flask_login import login_required
from flask_sqlalchemy import SQLAlchemy
from schemas.schemas import HabitSchema, UserSchema
from models.models import Habit
from templates import *
from api.config import *
import sqlalchemy as sa
from db import get_db, sessionmaker

db = get_db()


entry = Blueprint('entry', __name__)
@entry.route('/')
@entry.route('/index')
def index():

    return "hello there, login" 
@entry.route('/habits', methods=['POST'])
#@login_required
def add_habit():

    habit = request.json['habit']
    desc = request.json['desc']
    print(habit, desc)
    new_habit = Habit(habit=habit,desc=desc)
    print("hello1")
    db.add(new_habit)
    print("hello2")
    db.flush()
    print("hello34")
    db.refresh(new_habit)
    print("hello3")
    db.commit()
    print("hello")
    return HabitSchema.jsonify(new_habit) #return to client


@entry.route('/habits', methods=['GET'])
#@login_required
def get_habit(id):
    habit = habit.query.get(id)
    return HabitSchema.jsonify(habit)

@entry.route('/habits/<id>',methods=['POST'])
#@login_required
def update_habit(id):
    habit = habit.query.get(id)

    habit = request.json['habit']
    desc = request.json['desc']

    habit.habit = habit  
    habit.desc = desc

    db.commit()

    return HabitSchema.jsonify(habit)

@entry.route('/habits/<id>', methods=['DELETE'])
#@login_required
def delete_habit(id):
    habit = Habit.query.get(id)
    db.delete(habit)
    db.commit()
    return HabitSchema.jsonify(habit)