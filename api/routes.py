from flask import render_template
from app import app
from api import auth 

@app.route('/login')
def login():
    form = auth()
    return render_template('login.html', title='Sign In', form=form)