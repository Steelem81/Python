from doctest import debug_script
from flask import Flask, render_template, redirect, request
from users import User

app = Flask(__name__)
app.secret_key = 'pepperonipizza'

@app.route('/')
def users():
    all_users = User.get_all()
    return render_template('users.html', all_users = all_users)

@app.route('/add_user')
def add_user():
    return render_template('create_user.html')


@app.route('/create_user', methods=['POST'])
def create_user():
    data = {
        'fname': request.form['first_name'],
        'lname': request.form['last_name'],
        'email': request.form['email']
    }
    User.new_user(data)
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True, port=5001)