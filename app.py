from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'you-will-never-guess'

    from db import get_db
    db = get_db()

    
    migrate = Migrate(app,db) 
    from api import entry, auth
    app.register_blueprint(entry.entry)
    app.register_blueprint(auth.auth)
    return app
app = create_app()
login = LoginManager(app)
login.login_view = 'login'
from models import User

@login.user_loader
def load_user(user_id):
    # Replace this with your own logic to load the user object
    return User.query.get(int(user_id))

if __name__ == '__main__':
    app.run(debug=True)