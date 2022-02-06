from flask import render_template, request
from run import app
from models import Category, Pitch
from datetime import date
from run import db


@app.route('/add-pitch')
def form_pitch():
    categories = Category.query.all()
    return render_template('pitch_form.html', categories=categories)


@app.route('/')
def get_all_pitches():
    pitches = Pitch.query.all()
    return render_template('pitches.html', pitches=pitches)


@app.route('/', methods=['POST'])
def add_pitch():
    categories = Category.query.all()
    if request.method == 'POST':
        category = request.form['category']
        heading = request.form['name']
        description = request.form['pitch']
        posted = date.today()
        upvote = 0
        downvote = 0

        if category == '---select category---' or description == '' or heading == '':
            return render_template("pitch_form.html", message="Please enter required fields", categories=categories)
        else:
            pitch = Pitch(category, heading, description, posted, upvote, upvote)
            db.session.add(pitch)
            db.session.commit()
            return render_template('pitches.html')


@app.route('/auth/login')
def login():
    return render_template('auth/login.html')


@app.route('/auth/register')
def register():
    return render_template('auth/register.html')
