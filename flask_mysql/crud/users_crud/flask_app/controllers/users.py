from flask_app import app
from flask import render_template, request, redirect, url_for
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template('users.html', all_users = User.get_all_users())

#Show singlue user
@app.route('/users/<user_id>/show')
def show_user(user_id):
    return render_template('show_user.html', shown_user = User.get_one_user(user_id))


#Edit user
@app.route('/users/<user_id>/edit')
def edit_user(user_id):
    return render_template('update_user.html', updated_user = User.get_one_user(user_id))

@app.route('/update_user', methods=['POST'])
def update_user():
    updated_user_id = User.update_user(request.form)
    return redirect(url_for('show_user', user_id = updated_user_id))


#Create user
@app.route('/users/new')
def new_user():
    return render_template('create_user.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    new_user_id = User.add_user(request.form)
    return redirect(url_for('show_user', user_id = new_user_id))


#Delete user
@app.route('/users/<user_id>/delete')
def delete_user(user_id):
    User.del_user(user_id)
    return redirect('/users')


