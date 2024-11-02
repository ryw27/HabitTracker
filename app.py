from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from markupsafe import escape
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__)) #database directory

#set up database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'db.sqlite') #look for db.sqlite in folder structure
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#init db
db = SQLAlchemy(app)

#marshmallow
ma = Marshmallow(app)
# class User(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     username = db.Column(db.String(50),unique=True)
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True) # assign fields
    name = db.Column(db.String(100), unique=True)
    task = db.Column(db.String(100),unique=True)
    days = db.Column(db.Integer)

    def __init__(self,name,task,days):
        self.name = name
        self.task = task
        self.days = days

class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id','name','task','days') #what ppl are allowed to see    

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


#create a task
@app.route('/task', methods=['POST'])
def add_task():
    name = request.json['name']
    task = request.json['task']
    days = request.json['days']

    new_task = Task(name,task,days)
    db.session.add(new_task)
    db.session.commit()
    return task_schema.jsonify(new_task) #return to client

@app.route('/task', methods=['GET'])
def get_tasks():
    all_tasks = Task.query.all()
    result = tasks_schema.dump(all_tasks)
    return result
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

