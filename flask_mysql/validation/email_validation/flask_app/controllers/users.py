from flask import render_template, redirect, request
from flask_app.models import user
from flask_app import app

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def show_users():
    return render_template('users.html', all_users = user.User.get_all_users(), show_modal = False)

@app.route('/users/new_user')
def new_user():
    return render_template('/users.html', all_users = user.User.get_all_users(), show_modal = True)

@app.route('/add_user', methods=['POST'])
def add_user():
    user_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    print(user_data)
    if not user.User.validate_user(user_data):
        return redirect('/users')
    user.User.add_user(user_data)
    return redirect('/users')
