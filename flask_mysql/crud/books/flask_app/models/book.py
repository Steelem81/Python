from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors_favorited = []

    @classmethod
    def get_book(cls, book_data):
        query = "SELECT * FROM books LEFT OUTER JOIN favorites ON books.id = favorites.book_id LEFT OUTER JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(book_id)s;"
        results = connectToMySQL('books_schema').query_db(query, book_data)
        book = cls(results[0])
        for row in results:
            book.authors_favorited.append(author.Author(row))
        print(book.authors_favorited)
        return book

    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_schema').query_db(query)
        all_books = []
        for row in results:
            all_books.append(cls(row))
        return all_books

    @classmethod
    def save_book(cls, book_data):
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"
        return connectToMySQL('books_schema').query_db(query, book_data)
