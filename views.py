from flask import render_template, request, redirect, url_for
from run import app
from models import Category, Pitch, User
from datetime import date
from run import db
from flask_login import login_user, logout_user, login_required, current_user
from forms import LoginForm, RegistrationForm
from run import bcrypt


@app.route('/pitch-form')
def form_pitch():
    categories = Category.query.all()
    return render_template('pitch_form.html', categories=categories)


@app.route('/')
def get_all_pitches():
    pitches = Pitch.query.all()
    return render_template('pitches.html', pitches=pitches)


@app.route('/add-pitch', methods=['POST'])
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
            pitches = Pitch.query.all()
            return render_template('pitches.html', pitches=pitches )


@app.route('/register', methods=['GET', 'POST'])
def register_user():
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        password_hash = bcrypt.generate_password_hash(register_form.password.data).decode('utf8')
        user = User(email=register_form.email.data, username=register_form.username.data, password=password_hash)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('auth/register.html', form=register_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, login_form.password.data):
                login_user(user)
                pitches = get_all_pitches()
                return render_template('pitches.html', pitches=pitches)
    return render_template('auth/login.html', form=login_form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()
    return render_template("profile.html", user=user)