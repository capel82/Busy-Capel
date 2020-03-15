import os
import math
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
from werkzeug.security import generate_password_hash, \
    check_password_hash
#---- forms extension-flask WTF----#

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from forms import RegistrationForm, LoginForm, RecipesForm
#---- secret keys for MongoDB Atlas----#
import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Cluster0'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
mongo = PyMongo(app)

@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template("index.html", title='Homepage', recipes=mongo.db.recipes.find().limit(4))


#----- READ ALL RECIPES -----#
@app.route('/allrecipes/', methods=['GET', 'POST'])
@app.route('/allrecipes/<page>/<limit>', methods=['GET', 'POST'])
def allrecipes(page=1, limit=8):

    limit = int(limit)

    if request.method == 'POST':
        limit = int(request.form['limit'])
        
    page = int(page)
    skip = page * limit - limit
    maximum = math.ceil( (mongo.db.recipes.count_documents({})) / limit)

    recipes = list(mongo.db.recipes.find().skip(skip).limit( limit ))
    return render_template(
        'allrecipes.html',
        title='Recipes',
        recipes=recipes,
        page=page,
        pages=range(1, maximum + 1),
        maximum=maximum, limit=limit
    )
#----READ SINGLE RECIPE----#
@app.route('/show_recipe/<recipe_id>', methods=['GET', 'POST'])
def show_recipe(recipe_id):
 
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template(
        'recipe.html', recipe=the_recipe)

#----ROUTE TO REGISTER NEW ACCOUNT ----#
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():

        users = mongo.db.users
        existing_user = users.find_one({'email': request.form['email']})

        if existing_user is None:
            hash_pass = generate_password_hash(request.form['password'])
            users.insert_one({
                'email': request.form['email'].lower(),
                'password': hash_pass,})

            session['email'] = request.form['email']
            session['logged_in'] = True
            flash(f'Account created successfully for {form.email.data}!', 'success')
            return redirect(url_for('register'))
        
        else:
            flash('Sorry, email has already taken. Please try another.')
        return redirect(url_for('register'))

    return render_template('register.html', title='Register', form=form)

#---ROUTE TO LOGIN PAGE ----#
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        users = mongo.db.users
        existing_user = users.find_one({'email': request.form['email']})

        if existing_user:
            if check_password_hash(existing_user['password'],
                                   request.form['password']):
                session['email'] = request.form['email']
                session['logged_in'] = True
                flash(f'Login successfull for {form.email.data}!', 'success')
                return redirect(url_for('allrecipes'))
            else:
                flash('Login Unsuccessful. Please check email address and password', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', title='login', form=form)

#---ROUTE TO ACCOUNT PAGE ----#
@app.route('/account', methods=['GET', 'POST'])
def account():
    user_account = session['email']
    query = ({'email': user_account})
    my_recipes = mongo.db.users_recipes.find(query)
    return render_template('account.html', recipes=my_recipes)

@app.route('/show_myrecipe/<account_id>', methods=['GET', 'POST'])
def show_myrecipe(account_id):
 
    my_recipe = mongo.db.users_recipes.find_one({'_id': ObjectId(account_id)})
    return render_template('myrecipes.html', recipe=my_recipe)

#---ROUTE TO LOGOUT ---#
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('homepage'))    

#---ROUTE TO ADD RECIPE PAGE ----#
@app.route('/addrecipes', methods=['GET', 'POST'])
def addrecipes():
    form = RecipesForm(request.form)
    users_recipes = mongo.db.users_recipes

    if request.method == 'GET':
        return render_template('addrecipes.html', form=form,
                               title='Add Recipe')

    if request.method == 'POST':
        new_recipe = {
            'recipe_name': request.form.get('recipe_name'),
            'categories': request.form.get('categories'),
            'preparation_time': request.form.get('preparation_time'),
            'cooking_time': request.form.get('cooking_time'),
            'ingredients':request.form.getlist ('ingredients'),
            'methods': request.form.getlist('methods'),
            'notes': request.form.getlist('notes'),
            'email': session['email']
            }
        users_recipes.insert_one(new_recipe)
        flash('Your recipe saved!','success')
        return render_template ('addrecipes.html', recipe=new_recipe, form=form)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(8000),
            debug=True)
