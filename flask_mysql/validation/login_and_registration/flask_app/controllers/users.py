from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user

@app.route('/')
def index():
    if 'user_id' not in session:
        return render_template('index.html')
    else: 
        return redirect('dashboard.html')

@app.route('/register', methods=['POST'])
def f_register():
    data = {
        'first_name': request.form['fname'],
        'last_name': request.form['lname'],
        'email': request.form['email'],
        'password': request.form['password'],
        'confirm': request.form['confirm']
    }
    user.User.validate_user_registration(data)
    user.User.save_user(data)
    return redirect('/')

@app.route('/dashboard')
def r_dashboard():
    data = {
        'id': session['user_id']
    }
    thisUser = user.User.get_user_by_id(data)
    return render_template('dashboard.html', all_users = user.User.get_all_users(), thisUser = thisUser)

@app.route('/login', methods=['POST'])
def f_login():
    data = {
        'email': request.form['email']
    }
    if user.User.validate_user_login(request.form):
        thisUser = user.User.get_user_by_email(data)
        session['user_id'] = thisUser.id
        # if request.form['password'] != thisUser.password:
        #     flash("Password does not match")
        return redirect('/dashboard')
    else:
        return redirect('/')

@app.route('/logout')
def p_logout():
    session.clear()
    return redirect('/')

