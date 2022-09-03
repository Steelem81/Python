from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in result:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one_dojo_with_ninjas(cls, dojo_data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(dojo_id)s"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, dojo_data)
        dojo = cls(results[0])
        for row in results:
            ninja_data = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at']
                ,'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo

    @classmethod
    def new_dojo(cls, new_dojo_data):
        query = "INSERT INTO dojos (name) VALUES(%(dojo_name)s)"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, new_dojo_data)

    