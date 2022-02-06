from flask import render_template, request
from run import app
from models import Category, Pitch
from datetime import date
from run import db


@app.route('/')
def form_pitch():
    categories = Category.query.all()
    return render_template('pitch_form.html', categories=categories)


@app.route('/submit', methods=['POST'])
def add_pitch():
    categories = Category.query.all()
    if request.method == 'POST':
        category = request.form['category']
        description = request.form['pitch']
        posted = date.today()

        if category == '---select category---' or description == '':
            return render_template("pitch_form.html", message="Please enter required fields", categories=categories)
        else:
            pitch = Pitch(category, description, posted)
            db.session.add(pitch)
            db.session.commit()
            return render_template('pitches.html')

