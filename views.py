from flask import render_template
import requests
from run import app


@app.route('/')
def form_pitch():
    return render_template('pitch_form.html')


@app.route('/submit', methods=['POST'])
def add_pitch():
    requests.add_pitch()
    return render_template('pitch_form.html', message=requests.message)