from flask_app import app
from flask import render_template, redirect, request, url_for, session
from flask_app.models import ninja, dojo

@app.route('/ninja/add')
def add_ninja():
    return render_template('new_ninja.html', dojos=dojo.Dojo.get_all_dojos())

@app.route('/ninja/new', methods=['POST'])
def new_ninja():
    ninja_data = {
        'dojo_id': request.form['dojo_id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    dojo_id = request.form['dojo_id']
    session['dojo_id'] = dojo_id
    print(dojo_id)
    ninja.Ninja.save_ninja(ninja_data)
    return redirect(url_for('show_dojo', dojo_id = dojo_id))