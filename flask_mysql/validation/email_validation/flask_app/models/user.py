from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @staticmethod
    def validate_user(user):
        is_Valid = True
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        if not any(user.values()):
            flash("Please fill in all fields")
            is_Valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address")
            is_Valid = False
        return is_Valid
        


    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('users').query_db(query)
        all_users = []
        for row in results:
            all_users.append(cls(row))
        return all_users
    
    @classmethod
    def add_user(cls, user_data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        return connectToMySQL('users').query_db(query, user_data)