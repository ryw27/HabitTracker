from flask import Blueprint, request, redirect, render_template
from flask_login import login_required
from schemas import HabitSchema, HabitsSchema
from models import Habit
from config import *
from db import get_db
from app import *
import sqlalchemy as sa

entry = Blueprint("entries",__name__,url_prefix="entries")
db = get_db()

@entry.route('/')
@entry.route('/index')
def index():
    return render_template('index.html',title='Habits')
@app.route('/habits', methods=['POST'])
@login_required
def add_habit():
    habit = request.json['name']
    desc = request.json['desc']

    new_habit = Habit(habit,desc)
    db.session.add(new_habit)
    db.session.commit()
    return HabitSchema.jsonify(new_habit) #return to client

@app.route('/habits', methods=['GET'])
@login_required
def get_habits():
    all_habits = db.query.all()
    result = HabitsSchema.dump(all_habits) 
    return result

@app.route('/habits',methods=['GET'])
@login_required
def get_habit(id):
    habit = habit.query.get(id)
    return task_schema.jsonify(habit)

@app.route('/task/<id>',methods=['POST'])
@login_required
def update_habit(id):
    habit = habit.query.get(id)

    habit = request.json['habit']
    desc = request.json['desc']

    habit.habit = habit  
    habit.desc = desc

    db.session.commit()

    return task_schema.jsonify(task)

@app.route('/task/<id>', methods=['DELETE'])
@login_required
def delete_habit(id):
    habit = Habit.query.get(id)
    db.session.delete(habit)
    db.session.commit()
    return task_schema.jsonify(habit)