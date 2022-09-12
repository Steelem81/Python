from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import user
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not user.User.validate_register(request.form) is True:
        return redirect('/')
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    id = user.User.save_user(data)
    session['user_id'] = id
    return redirect('/recipes')

@app.route('/login', methods=['POST'])
def login():
    current_user = user.User.get_user_by_email(request.form)

    if not user:
        flash('Invalid email', 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(current_user.password, request.form['password']):
        flash("Invalid password", 'login')
        return redirect('/')
    session['user_id'] = current_user.id
    session['first_name'] = current_user.first_name
    return redirect('/recipes')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')