from run import db
from run import login_manager
from flask_login import UserMixin
from run import bcrypt


class Pitch(db.Model):
    __tablename__ = "pitches"
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    heading = db.Column(db.String(255))
    description = db.Column(db.String(255))
    posted = db.Column(db.Date)
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    name = db.Column(db.String(255))

    def __init__(self, category, heading, description, posted,up_vote, down_vote, name):
        self.category_id = category
        self.heading = heading
        self.description = description
        self.posted = posted
        self.upvote = up_vote
        self.downvote = down_vote
        self.name = name


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

    def set_password(self, pw):
        pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
        self.password = pwhash.decode('utf8')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    comment_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    name = db.Column(db.String(255))
    desc = db.Column(db.String(255))

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
