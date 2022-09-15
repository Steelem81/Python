from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user, comment

class Post:
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.comments = []
        self.user = None

    @staticmethod
    def validate_post(post):
        is_valid = True
        if len(post['content']) <= 0:
            is_valid = False
            flash("Silence maybe golden, but we need content", "post")
        return is_valid

    @classmethod
    def get_all_posts(cls):
        query = "SELECT * FROM posts LEFT OUTER JOIN users ON posts.USER_ID = users.ID;"
        results = connectToMySQL('dojo_wall').query_db(query)
        all_posts=[]
        for row in results:
            post_obj = cls(row)
            print(post_obj.id)
            post_obj.user = user.User.get_user_by_id(data={'id': row['user_id']})
            post_obj.comments = comment.Comment.get_all_comments_by_post(data={'post_id':post_obj.id})
            all_posts.append(post_obj)
            return all_posts
    
    @classmethod
    def save_post(cls, data):
        query = "INSERT INTO posts (content, user_id) VALUES (%(content)s, %(user_id)s);"
        return connectToMySQL('dojo_wall').query_db(query, data)

    @classmethod
    def delete_post(cls, data):
        query = "DELETE * FROM posts WHERE id = %(id)s;"
        return connectToMySQL('dojo_wall').query_db(query, data)
