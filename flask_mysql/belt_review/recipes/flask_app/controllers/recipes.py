from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models import user, recipe

@app.route('/recipes')
def recipes():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
            }
    return render_template('recipes.html', user=user.User.get_user_by_id(data), all_recipes=recipe.Recipe.get_all_recipes())

@app.route('/recipes/new')
def new_recipe():
    return render_template('create_recipe.html')

@app.route('/recipes/create', methods=['POST'])
def create_recipe():
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'under_30': request.form['under_30'],
        'user_id': session['user_id']
    }
    print(data)
    recipe.Recipe.save_recipe(data)
    return redirect('/recipes')

@app.route('/recipes/<recipe_id>')
def get_recipe(recipe_id):
    data = {
        'id': recipe_id
    }
    this_recipe = recipe.Recipe.get_recipe(data)
    print(this_recipe.user_id)
    user_data = {
        'id': this_recipe.user_id
    }
    recipe_user = user.User.get_user_by_id(user_data)
    return render_template('recipe.html', recipe = this_recipe, user = recipe_user)

@app.route('/recipes/delete/<recipe_id>')
def delete_recipe(recipe_id):
    data={
        'id': recipe_id
    }
    recipe.Recipe.delete_recipe(data)
    return redirect('/recipes')

@app.route('/recipes/edit/<recipe_id>')
def edit_recipe(recipe_id):
    data = {
        'id': recipe_id
    }
    this_recipe = recipe.Recipe.get_recipe(data)
    return render_template('edit_recipe.html', recipe = this_recipe)

@app.route('/recipes/update', methods=['POST'])
def update_recipe():
    data={
        'id': request.form['id'],
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'under_30': request.form['under_30'],
        'user_id': session['user_id']
    }
    recipe.Recipe.update_recipe(data)
    return redirect('/recipes')