from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://joshua:letmein@localhost/joshua'
    app.config['SECRET_KEY'] = "1234567"
else:
    app.debug == False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
    app.config['SECRET_KEY'] = "1234567"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
bcrypt = Bcrypt(app)


from views import *

if __name__ == '__main__':
    app.run(debug=True)
