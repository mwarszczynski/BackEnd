from datetime import datetime
from flask import current_app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def initialize_db(app):
    app.app_context().push()
    db.init_app(app)
    db.create_all()


books_authors = db.Table('BooksAuthors',
                         db.Column('book_id', db.Integer,
                                   db.ForeignKey('book.id')),
                         db.Column('author_id', db.Integer,
                                   db.ForeignKey('authors.id'))
                         )


books_categories = db.Table('BooksCategories',
                            db.Column('book_id', db.Integer,
                                      db.ForeignKey('book.id')),
                            db.Column('category_id', db.Integer,
                                      db.ForeignKey('category.id'))
                            )


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=False)
    describe = db.Column(db.String(150), unique=False)
    ba = db.relationship('Authors', secondary=books_authors,
                         backref=db.backref('auth_book', lazy='dynamic'))
    bc = db.relationship('Category', secondary=books_categories,
                         backref=db.backref('cat_book', lazy='dynamic'))

    def __init__(self, title, describe):
        self.title = title
        self.describe = describe


class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False)

    def __init__(self, name):
        self.name = name


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(20), unique=False)

    def __init__(self, species):
        self.species = species


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
#     password = db.Column(db.String(60), nullable=False)
#     posts = db.relationship('Post', backref='author', lazy=True)

#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}', '{self.image_file}')"
