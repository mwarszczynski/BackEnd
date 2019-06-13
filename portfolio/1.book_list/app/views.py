from app import app

from flask import render_template, request, redirect, jsonify, make_response

from datetime import datetime

from . import db, Book, Authors, Category

@app.template_filter('clean_date')
def clean_date(dt):
    return dt.strftime('%d %b %Y')


@app.route("/")
def index():
        return render_template("public/index.html")


@app.route("/list_of_books")
def list_of_books():
        books = Book.query.all()
        authors = Authors.query.all()
        categories = Category.query.all()
        return render_template("public/list_of_books.html",
                                books=books, authors=authors,
                                categories=categories)


@app.route("/add_book", methods=['GET'])
def add_book():
    return render_template("public/add_book.html")


@app.route('/add_book_post', methods=['POST'])
def add_book_post():
        book1 = Book()
        book1.title = request.form['title']

        author1 = Authors()
        author1.name = request.form['author']

        category1 = Category()
        category1.species = request.form['species']

        db.session.add(book1)
        db.session.add(author1)
        db.session.add(category1)

        db.session.commit()

        return render_template("public/add_book_post.html")
 

@app.route("/import_book")
def import_book():
    return render_template("public/import_book.html")


@app.route('/correct_login', methods=['GET', 'POST'])
def correct_login():

    if request.method == 'POST':

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

    return render_template('admin/correct_login.html',
                            username=username, email=email, 
                            password=password)





