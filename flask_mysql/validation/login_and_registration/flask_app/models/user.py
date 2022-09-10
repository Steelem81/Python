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

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('users_lnr').query_db(query)
        all_users = []
        for row in results:
            all_users.append(cls(row))
        return all_users

    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('users_lnr').query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('users_lnr').query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def save_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        flash("User saved")
        return connectToMySQL('users_lnr').query_db(query, data)

    @staticmethod
    def validate_user_registration(user):
        isValid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('users_lnr').query_db(query, user)
        if len(results) >= 1:
            isValid = False
            flash("It looks like your email addrees is already in use. Please try logging in", 'registration')
        if len(user['first_name']) < 2:
            isValid = False
            flash("Please use at least 2 characters for your first name", 'registration')
        if len(user['last_name']) < 2:
            isValid = False
            flash("Please use at least 2 characters for your last name", 'registration')
        if len(user['email']) < 6:
            isValid = False
            flash("Please use at least 6 characters for your email", 'registration')
        if not EMAIL_REGEX.match(user['email']):
            isValid = False
            flash("Please enter a valid email", 'registration')
        if user['password'] != user['confirm']:
            isValid = False
            flash("Passwords do not match", 'registration')
        return isValid

    @staticmethod
    def validate_user_login(data):
        is_valid = True
        if not data['email']:
            is_valid = False
            flash("Please enter a valid email", 'login')
        if not data['password']:
            is_valid = False
            flash("Please enter a valid password", 'login')
        return is_valid
        