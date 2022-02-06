from flask import request
from flask_sqlalchemy import SQLAlchemy


def add_pitch():
    if request.method == 'POST':
        category = request.form['category']
        description = request.form['pitch']





