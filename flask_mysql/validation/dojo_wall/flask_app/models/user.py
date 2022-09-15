from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import post
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
        self.posts = []

    @staticmethod
    def validate_register(data):
        is_valid = True
        if len(data['first_name'])< 2:
            is_valid = False
            flash("First name must be longer than 2 characters", "register")
        if len(data['last_name']) < 2: 
            is_valid = False
            flash("Last name must be longer than 2 characters", "register")
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash("Please enter a valid email address", "register")
        if data['password'] != data['confirm']:
            is_valid = False
            flash("Passwords do not match", "register")
        return is_valid

    @classmethod
    def save_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL('dojo_wall').query_db(query, data)

    @classmethod
    def get_user_by_email(cls, data):
        print("IN THE METHOD")
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('dojo_wall').query_db(query, data)
        print(results)
        return cls(results[0])

    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL('dojo_wall').query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('dojo_wall').query_db(query)
        all_users = []
        for row in results:
            all_users.append(cls(row))
        return all_users