from . import db
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    ID = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), unique=True, nullable=False)
    firstname = db.Column(db.String(60), nullable=False)
    lastname = db.Column(db.String(60), nullable=False)
    middlename = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    books = db.relationship('Books')

    def get_id(self):
        return (self.ID)

class Books(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Book_name = db.Column(db.String(60), unique=True, nullable=False)
    Book_author = db.Column(db.String(60))
    date_added = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.ID"))

    def get_id(self):
        return (self.ID)
