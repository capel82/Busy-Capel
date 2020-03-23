import os
import math
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
from werkzeug.security import generate_password_hash, \
    check_password_hash
#---- forms extension-flask WTF----#
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, Optional, EqualTo
from forms import RegistrationForm, LoginForm, RecipesForm
#---- secret keys for MongoDB Atlas----#
if os.path.exists("env.py"):
    import env
''
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Cluster0'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
mongo = PyMongo(app)

#----ROUTE TO HOMEPAGE----#
@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template("index.html", title='Homepage', recipes=mongo.db.recipes.find().limit(4))

#----CRUD OPERATION: Create----#
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

    #---ROUTE TO ADD RECIPE PAGE ----#
@app.route('/addrecipes', methods=['GET', 'POST'])
def addrecipes():
    form = RecipesForm(request.form)
    users_recipes = mongo.db.users_recipes
    
    if request.method == 'GET':
        return render_template('addrecipes.html', form=form,
                               title='Add Recipe')
                               
    ingredients = request.form.get('ingredients').splitlines()
    methods = request.form.get('methods').splitlines()

    if request.method == 'POST':
        new_recipe = {
            'recipe_name': request.form.get('recipe_name'),
            'categories': request.form.get('categories'),
            'serving_portion': request.form.get('serving_portion'),
            'preparation_time': request.form.get('preparation_time'),
            'cooking_time': request.form.get('cooking_time'),
            'ingredients': ingredients,
            'methods': methods,
            'notes': request.form.getlist('notes'),
             'email': session['email']
            }
        users_recipes.insert_one(new_recipe)
        flash('Your recipe saved!','success')
        return redirect(url_for('account'))
        return render_template ('addrecipes.html', recipe=new_recipe, form=form)

#----CRUD OPERATION: Read----#
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
    #----READ STARTERS CATEGORIES----#
@app.route('/starter')
def starter():
         starter = mongo.db.recipes.find ({'categories': 'Starter'})
         return render_template('starter.html',
                           categories=starter)
    #----READ MAINS CATEGORIES----#
@app.route('/mains')
def mains():
         mains = mongo.db.recipes.find ({'categories': 'Main'})
         return render_template('mains.html',
                           categories=mains)

    #----READ DESSERTS CATEGORIES----#
@app.route('/desserts')
def desserts():
         desserts = mongo.db.recipes.find ({'categories': 'Dessert'})
         return render_template('desserts.html',
                           categories=desserts)
                           

    #---READ ACCOUNT PAGE ----#
@app.route('/account', methods=['GET', 'POST'])
def account():
    user_account = session['email']
    query = ({'email': user_account})
    my_recipes = mongo.db.users_recipes.find(query)
    return render_template('account.html', recipes=my_recipes)
    #---READ USER RECIPES PAGE ----#
@app.route('/show_myrecipe/<account_id>', methods=['GET', 'POST'])
def show_myrecipe(account_id):
    my_recipe = mongo.db.users_recipes.find_one({'_id': ObjectId(account_id)})
    return render_template('myrecipes.html', recipe=my_recipe)
#----CRUD OPERATION: Update----#
@app.route('/edit_myrecipe/<account_id>', methods=['GET', 'POST'])
def edit_myrecipe(account_id):
    users_recipes = mongo.db.users_recipes
    edit_recipe = users_recipes.find_one({'_id': ObjectId(account_id)})
    form = RecipesForm(data=edit_recipe)

    return render_template('edit_myrecipe.html', recipe=edit_recipe, form=form)

@app.route('/update_myrecipe/<account_id>', methods=['POST'])
def update_myrecipe(account_id):
    form = RecipesForm(request.form)
    users_recipes = mongo.db.users_recipes

    if request.method == 'POST':
        recipe = users_recipes.find_one({'_id': ObjectId(account_id)})
        ingredients = request.form.get('ingredients').splitlines()
        methods = request.form.get('methods').splitlines()

        users_recipes.update({'_id': ObjectId(account_id)}, {
            'recipe_name': request.form.get('recipe_name'),
            'categories': request.form.get('categories'),
            'preparation_time': request.form.get('preparation_time'),
            'cooking_time': request.form.get('cooking_time'),
            'ingredients':ingredients,
            'methods': methods,
            'notes': request.form.getlist('notes'),
            'email': session['email']
            })
        flash('Your recipe updated!','success')
        return redirect(url_for('account', recipe_id=account_id)) 
        return render_template ('myrecipes.html', recipe=recipe, form=form)

#----CRUD OPERATION: Delete----#
@app.route('/delete_recipe/<account_id>', methods=['GET', 'POST'])
def delete_recipe(account_id):
    mongo.db.users_recipes.remove({'_id': ObjectId(account_id)})
    flash('Your recipe has been deleted!', 'warning')
    return redirect(url_for('account'))

#---ROUTE TO LOGOUT ---#
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('homepage'))    

if __name__ == '__main__':
    app.run(os.environ.get('IP', '0.0.0.0'),
            int(os.environ.get('PORT', '5000'),
            debug=True))
