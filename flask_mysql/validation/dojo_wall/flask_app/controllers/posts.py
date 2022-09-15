from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models import post,comment

@app.route('/wall')
def wall():
    return render_template('wall.html', all_posts = post.Post.get_all_posts())

@app.route('/posts/publish', methods=['POST'])
def publish_post():
    data = {
        'content': request.form['content'],
        'user_id': session['user_id']
    }
    post.Post.save_post(data)
    return redirect('/wall')

@app.route('/posts/comment', methods=['POST'])
def comment():
    flash('comment_posted', 'post')
    data = {
        'post_id': request.form['post_id'],
        'comment': request.form['comment'],
        'user_id': session['user_id']
    }
    print(data)
    comment.Comment.new_comment(data)
    return redirect('/wall')

@app.route('/posts/delete/<post_id>')
def delete_post(post_id):
    post.Post.delete_post(data={'id': post_id})
    return redirect('/wall')
