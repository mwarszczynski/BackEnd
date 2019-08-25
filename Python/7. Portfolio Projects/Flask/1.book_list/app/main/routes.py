from flask import render_template, request, Blueprint, flash, url_for, redirect, jsonify
from app.models import db
from app.models import books_authors, Book, Authors, Category

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("home.html")


@main.route("/list_of_books", methods=["GET"])
def list_of_books():

    books = Book.query.all()
    authors = Authors.query.all()
    categories = Category.query.all()

    return render_template("list_of_books.html",
                           books=books, authors=authors, categories=categories)


@main.route("/list_of_books/<int:id>", methods=["GET"])
def list_of_book(id):

    book = Book.query.filter_by(id=id).first()

    return render_template("list_of_books.html",
                            id=id)


@main.route("/add_book", methods=["GET"])
def add_book():
    return render_template("add_book.html")


@main.route("/add_book_post", methods=["GET", "POST"])
def add_book_post():

    if request.method == "POST":
        if not request.form['title'] or not request.form['describe'] or not request.form['name'] or not request.form['species']:
            flash('You have to enter all fields!')
        else:
            book = Book(request.form['title'], request.form['describe'])
            author = Authors(name=request.form.get("name"))
            category = Category(species=request.form.get("species"))

            db.session.add(book)
            db.session.add(author)
            db.session.add(category)

            # Pushing data to 'pivot' tables
            author.auth_book.append(book)
            category.cat_book.append(book)

            db.session.commit()
            flash('Successfully added')

    return render_template("add_book_post.html",
                           book=book, author=author,
                           category=category)


@main.route("/import_book")
def import_book():
    return render_template("import_book.html")
