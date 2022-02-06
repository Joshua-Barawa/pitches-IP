from flask import render_template, request
from run import app
from models import Category


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

        if category == '---select category---' or description == '':
            return render_template("pitch_form.html", message="Please enter required fields", categories=categories)
        else:
            return render_template('pitch_form.html', message="Please enter required fields", categories=categories)

