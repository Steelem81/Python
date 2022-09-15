from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, post
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/register', methods=['POST'])
def register():
    if not user.User.validate_register(request.form):
        return redirect('/')
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    this_user_id = user.User.save_user(data)
    session['user_id'] = this_user_id
    session['first_name'] = data['first_name']
    return redirect('/wall')

@app.route('/users/login', methods=['POST'])
def login():
    this_user = user.User.get_user_by_email(request.form)

    if not this_user:
        flash('Invalid email address', 'login')
    if not bcrypt.check_password_hash(this_user.password, request.form['password']):
        flash('Invalid password', 'loging')
    
    session['user_id'] = this_user.id
    session['first_name'] = this_user.first_name
    return redirect('/wall')

@app.route('/users/logout')
def logout():
    session.clear()
    return redirect('/')