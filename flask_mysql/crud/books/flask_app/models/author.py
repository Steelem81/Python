from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = []
    
    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_schema').query_db(query)
        all_authors = []
        for row in results:
            all_authors.append(cls(row))
        print(all_authors)
        return all_authors

    @classmethod
    def save_author(cls, author):
        query = "INSERT INTO authors (name) VALUES (%(author_name)s);"
        return connectToMySQL('books_schema').query_db(query, author)

    @classmethod
    def get_author_favorites(cls, author_data):
        query = "SELECT * FROM authors LEFT OUTER JOIN favorites ON authors.id = favorites.author_id LEFT OUTER JOIN books ON favorites.book_id = books.id WHERE authors.id = %(author_id)s;"
        results = connectToMySQL('books_schema').query_db(query, author_data)
        author = cls(results[0])
        for row in results:
            book_data = {
                'id': row['books.id'],
                'title': row['title'],
                'num_of_pages': row['num_of_pages'],
                'created_at': row['books.created_at'],
                'updated_at': row['books.updated_at']
            }
            author.favorite_books.append(book.Book(book_data))
        return author

    @classmethod
    def add_author_favorite(cls, favorites_data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES ( %(author_id)s, %(book_id)s);"
        return connectToMySQL('books_schema').query_db(query, favorites_data)
