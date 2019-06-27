from flask import render_template, request ,Blueprint

main = Blueprint('main', __name__)


@main.route("/")
def home():
    return render_template("home.html")


@main.route("/list_of_books")
def list_of_books():
    return render_template("list_of_books.html")


@main.route("/add_book", methods=['GET'])
def add_book():
    return render_template("add_book.html")
 

@main.route("/import_book")
def import_book():
    return render_template("import_book.html")