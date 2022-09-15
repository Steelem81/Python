from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import post

class Comment:
    def __init__(self, data):
        self.id = data['id']
        self.post_id = data['post_id']
        self.user_id = data['user_id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all_comments_by_post(cls, data):
        query = "SELECT * FROM comments WHERE post_id = %(post_id)s;"
        results = connectToMySQL('dojo_wall').query_db(query, data)
        all_posts = []
        for row in results:
            all_posts.append(cls(row))
        return all_posts

    @classmethod
    def save_comment(cls, data):
        query = "INSERT INTO comments (post_id, user_id, content) VALUES (%(post_id)s, %(user_id)s, %(content)s);"
        return connectToMySQL('dojo_wall').query_db(query,data)