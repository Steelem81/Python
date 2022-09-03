from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_ninja(cls, ninja_id):
        query = "SELECT * FROM ninjas WHERE id = %(ninja_id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, int(ninja_id))
        print(int(ninja_id))
        print(result)
        return 

    
    @classmethod
    def save_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def update_ninja(cls, ninja_data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s WHERE ninjas.id = %(ninja_id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, ninja_data)
    @classmethod
    def delete_ninja(cls, ninja_id):
        query = "DELETE FROM ninjas WHERE id = %(ninja_id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, ninja_id)