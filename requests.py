from flask import request,jsonify
from flask_sqlalchemy import SQLAlchemy


def add_pitch():
    if request.method == 'POST':
        category = request.form['category']
        description = request.form['pitch']






