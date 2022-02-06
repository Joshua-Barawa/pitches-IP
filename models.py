from run import db


class Pitch(db.Model):
    __tablename__ = "pitches"
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    heading = db.Column(db.String(255))
    description = db.Column(db.String(255))
    posted = db.Column(db.Date)

    def __init__(self, category, heading, description, posted):
        self.category_id = category
        self.heading = heading
        self.description = description
        self.posted = posted


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name
