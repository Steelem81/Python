from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []

    @staticmethod
    def validate_register(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('recipes_schema').query_db(query, user)
        if len(results) >= 1:
            is_valid = False
            flash("Email is already taken", "register")
        if len(user['first_name']) < 2:
            is_valid = False
            flash("First name must be at least 2 characters", "register")
        if len(user['last_name']) < 2:
            is_valid = False
            flash("Last name must be at least 2 characters", "register")
        if not EMAIL_REGEX.match(user['email']):
            is_valid = False
            flash("Email is not valid", "register")
        if user['password'] != user['confirm']:
            is_valid = False
            flash("Passwords do not match", "register")
        return is_valid

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('recipes_schema').query_db(query)
        all_users = []
        for row in results:
            all_users.append(cls(row))
        return all_users

    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('recipes_schema').query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL('recipes_schema').query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def save_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL('recipes_schema').query_db(query, data)
    
    