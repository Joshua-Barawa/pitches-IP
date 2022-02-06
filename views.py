from flask import render_template
import requests
from run import app
from models import Category


@app.route('/')
def form_pitch():
    categories = Category.query.all()
    return render_template('pitch_form.html', categories=categories)


@app.route('/submit', methods=['POST'])
def add_pitch():
    requests.add_pitch()
    return render_template('pitch_form.html', message=requests.message)