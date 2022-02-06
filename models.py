from run import db


class Pitch(db.Model):
    __tablename__ = "pitches"
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    heading = db.Column(db.String(255))
    description = db.Column(db.String(255))
    posted = db.Column(db.Date)
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)

    def __init__(self, category, heading, description, posted,upvote, down_vote):
        self.category_id = category
        self.heading = heading
        self.description = description
        self.posted = posted
        self.up_vote = upvote
        self.downvote = down_vote


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
