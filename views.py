import bcrypt
from flask import render_template, request, redirect, url_for
from run import app
from models import Category, Pitch, User
from datetime import date
from run import db
from flask_login import login_user, logout_user, login_required
from forms import LoginForm
from flask_bcrypt import Bcrypt


@app.route('/add-pitch')
def form_pitch():
    categories = Category.query.all()
    return render_template('pitch_form.html', categories=categories)


@app.route('/')
def get_all_pitches():
    pitches = Pitch.query.all()
    return render_template('pitches.html', pitches=pitches)


@app.route('/', methods=['POST'])
@login_required
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


@app.route('/auth/register')
def register():
    return render_template('auth/register.html')


@app.route('/auth/login', methods=['POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user is not None and user.verify_password(password):
            login_user(user)
            return render_template("auth/register.html", message="User already exists")
        else:
            user = User(email, username, password)
            db.session.add(user)
            db.session.commit()
            return render_template('auth/login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    return render_template('auth/login.html', form=login_form)


# @app.route('/loggedin', methods=['GET', 'POST'])
# def login_user():
#     login_form = LoginForm()



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))
