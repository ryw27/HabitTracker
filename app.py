from models import *
from flask import Flask
from flask_login import LoginManager

from flask_sqlalchemy import SQLAlchemy

def create_app():
    global app 

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'you-will-never-guess'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
    globaldb = SQLAlchemy(app) 

    login = LoginManager(app)
    login.login_view = 'login'
    app.register_blueprint(entry.entry)
    return app
app = create_app()
