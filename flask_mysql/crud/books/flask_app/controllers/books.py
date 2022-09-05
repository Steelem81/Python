from flask_app import app
from flask import render_template, redirect, request, url_for
from flask_app.models import book, author

@app.route('/books')
def books():
    return render_template("books.html", all_books  = book.Book.get_all_books())

@app.route('/book/new', methods=['POST'])
def new_book():
    book_data = {
        'title': request.form['book_title'],
        'num_of_pages': request.form['num_of_pages']
    }
    book.Book.save_book(book_data)
    return redirect('/books')

@app.route('/book/<book_id>')
def show_book(book_id):
    book_data = {
        'book_id': book_id
    }
    return render_template("book_info.html", book = book.Book.get_book(book_data), all_authors = author.Author.get_all_authors())

@app.route('/book/add_favorite', methods=['POST'])
def book_add_favorite():
    favorite_data = {
        'book_id': request.form['book_id'],
        'author_id': request.form['author_id']
    }
    author.Author.add_author_favorite(favorite_data)
    return redirect(url_for('show_book', book_id=favorite_data['book_id']))