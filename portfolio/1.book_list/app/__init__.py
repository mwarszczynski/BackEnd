from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:secret@env-db/STX'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

books_authors = db.Table('BooksAuthors',
    db.Column('user_id', db.Integer, db.ForeignKey('book.book_id')),
    db.Column('author_id', db.Integer, db.ForeignKey('authors.author_id'))
    )


class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(20), unique=False)
    bk = db.relationship('Authors', secondary=books_authors, backref=db.backref('subscribers', lazy='dynamic'))

    def __init(self, title):
        self.title = title
        

class Authors(db.Model):
    author_id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20), unique=False)

    def __init(self, first_name):
        self.first_name = first_name


class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key = True)
    species = db.Column(db.String(20), unique=False)

    def __init(self, species):
        self.species = species


from app import views
from app import admin_views