from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Recipe():
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        data = {
            'id': data['user_id']
        }
        self.user = user.User.get_user_by_id(data)
    
    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL('recipes_schema').query_db(query)
        all_recipes = []
        for row in results:
            all_recipes.append(cls(row))
        return all_recipes

    @classmethod
    def get_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL('recipes_schema').query_db(query, data)
        return (cls(results[0]))
    
    @classmethod
    def save_recipe(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, under_30, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(under_30)s, %(user_id)s);"
        return connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description=%(description)s, instructions=%(instructions)s, under_30= %(under_30)s WHERE id = %(id)s"
        return connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL('recipes_schema').query_db(query, data)