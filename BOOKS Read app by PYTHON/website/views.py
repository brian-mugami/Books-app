from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user, login_user
from .models import Books, User
from . import db
from .forms.webforms import SearchForm
import json


views = Blueprint("views", __name__, static_folder="static", template_folder="templates")

@views.route("/")
@views.route("/addbook", methods=["POST", "GET"])
@login_required
def add_book():
    if request.method == "POST":
        bookname = request.form.get("bookname")
        author = request.form.get("author")
        book = Books.query.filter_by(Book_name=bookname).first()
        if book:
            flash("This book already exists", category="error")
        elif len(author) < 1:
            flash("You need to input an author", category="error")
        else:
            new_book = Books(Book_name=bookname, Book_author=author, user_id=current_user.ID)
            db.session.add(new_book)
            db.session.commit()
            flash("Book added successfully", category="success")
            return render_template("books.jinja2", user=current_user)
    return render_template("loginhome.jinja2", user= current_user)

@views.context_processor
def base():
    form = SearchForm()
    return dict(form=form)

@views.route("/search", methods=["POST"])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        post = form.search.data
        books = Books.query.filter(Books.Book_name.like('%' + post + '%'))
        return render_template("search.jinja2", form=form, books=books, user=current_user)

@views.route("/mybooks")
def my_books():
    books = Books.query.order_by(Books.date_added)
    return render_template("yourreadbooks.jinja2", user=current_user, books=books)

@views.route("/allbooks")
def all_books():
    all_books = Books.query.order_by(Books.date_added)
    return render_template("allreadbooks.jinja2", user=current_user, books=all_books)

@views.route("/delete-note", methods=['POST'])
def delete_note():
    book = json.loads(request.data)
    bookid = book['bookid']
    book = Books.query.get(bookid)
    if book:
        if book.user_id == current_user.ID:
            db.session.delete(book)
            db.session.commit()

    return jsonify({})
