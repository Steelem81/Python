from flask_app import app
from flask import render_template, redirect, request, url_for
from flask_app.models import author, book

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    return render_template("authors.html", all_authors = author.Author.get_all_authors())

@app.route('/authors/new', methods=['POST'])
def new_author():
    author_data = {
        'author_name' :request.form['author_name']
    }
    author.Author.save_author(author_data)
    return redirect('/authors')
    
@app.route('/author/<author_id>')
def authors_favorites(author_id):
    author_data = {
        'author_id': author_id
    }
    return render_template("authors_favorites.html", author = author.Author.get_author_favorites(author_data), all_books = book.Book.get_all_books())

@app.route('/author/add_favorite', methods=['POST'])
def author_add_favorite():
    favorite_data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    author.Author.add_author_favorite(favorite_data)
    return redirect(url_for('authors_favorites', author_id = favorite_data.get('author_id')))