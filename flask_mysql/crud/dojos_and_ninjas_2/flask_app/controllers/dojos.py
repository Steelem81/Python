from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return redirect('/dojo')

@app.route('/dojo')
def dojos():
    return render_template('dojos.html', dojos_list = Dojo.get_all_dojos())

@app.route('/dojo/<dojo_id>')
def show_dojo(dojo_id):
    dojo_data = {
        'dojo_id': dojo_id
    }
    dojo = Dojo.get_one_dojo_with_ninjas(dojo_data)
    return render_template('dojo.html',dojo = Dojo.get_one_dojo_with_ninjas(dojo_data))

@app.route('/dojo/new', methods=['POST'])
def new_dojo():
    new_dojo_data ={
        'dojo_name': request.form['dojo_name']
    }
    Dojo.new_dojo(new_dojo_data)
    return redirect('/dojo')