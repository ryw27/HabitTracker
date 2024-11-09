import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #basedir = os.path.abspath(os.path.dirname(__file__))
    #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #    'sqlite:///' + os.path.join(basedir, 'app.db')