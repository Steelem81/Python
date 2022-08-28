from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('users').query_db(query)

        all_users = []
        for u in results:
            all_users.append(cls(u))
        return all_users

    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(fname)s, %(lname)s, %(email)s);"
        user_data = {
            'fname': data['fname'],
            'lname': data['lname'],
            'email': data['email']
        }
        return connectToMySQL('users').query_db(query, user_data)

    @classmethod
    def update_user(cls, data):
        query = "UPDATE users set first_name = %(fname)s, last_name = %(lname)s, email = %(email)s WHERE id = %(user_id)s"
        user_data = {
            'fname': data['fname'],
            'lname': data['lname'],
            'email': data['email'],
            'user_id': int(data['user_id'])
        }        
        connectToMySQL('users').query_db(query, user_data)
        return user_data['user_id']

    @classmethod
    def get_one_user(cls, user_id):
        query = "SELECT * FROM users WHERE id=%(id_num)s;"
        data = {
            'id_num': user_id,
        }
        result = connectToMySQL('users').query_db(query, data)
        return cls(result[0])


    @classmethod
    def del_user(cls, user_id):
        query = "DELETE FROM users WHERE id=%(user_id)s;"
        user_data = {
            'user_id': user_id
        }
        return connectToMySQL('users').query_db(query, user_data)