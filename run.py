import os
import math
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
from werkzeug.security import generate_password_hash, \
    check_password_hash
#forms extension-flask WTF
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, Optional, EqualTo
from forms import RegistrationForm, LoginForm
#secret keys for MongoDB Atlas
if os.path.exists("env.py"):
    import env
''
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Cluster0'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
mongo = PyMongo(app)

#ROUTE TO HOMEPAGE
@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template("index.html", title='Homepage', recipes=mongo.db.recipes.find().limit(4))

#CREATE:route to REGISTER PAGE using Flask-WTForms
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
            session['logged_in'] = False
            flash('Sorry, email has already taken. Please try another.')
        return redirect(url_for('register'))

    return render_template('register.html', title='Register', form=form)

#CREATE: Route to LOGIN PAGE using Flask_WTForms
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
                session['logged_in'] = False
                flash('Login Unsuccessful. Please check email address and password', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', title='login', form=form)

#CREATE: Route for ADD RECIPES - rendering the form in Add Recipe page
@app.route('/addrecipes', methods=['GET', 'POST'])
def addrecipes():
    users_recipes = mongo.db.users_recipes 

    return render_template("addrecipes.html",recipes=users_recipes.find())

#CREATE: Route to insert new recipe to mongodb database when submit button is clicked.
@app.route('/insert_recipes', methods=['POST'])
def insert_recipes():
    users_recipes = mongo.db.users_recipes
    if request.method == "POST":
        (request.form.to_dict())
        new_recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "categories": request.form.get("categories"),
            "preparation_time": request.form.get("preparation_time"),
            "cooking_time": request.form.get("cooking_time"),
            "serving_portion": request.form.get("serving_portion"),
            "ingredients": list(request.form.get("ingredients").split("\n")),
            "methods": list(request.form.get("methods").split("\n")),
            "notes": request.form.get("notes"),
            "email": session.get("email"),
        }
        users_recipes.insert_one(new_recipe)
        flash('Your New Recipe has been added into your account.', 'success')
        return redirect(url_for('account'))
    return render_template("addrecipes.html", recipes = new_recipe)

#READ:route to render all recipes in the Editor's database
#use pagination for better UX in displaying recipes
@app.route("/allrecipes")
def allrecipes():
    #pagination
    total = mongo.db.recipes.count()
    page_limit=8
    offset = int(request.args.get('offset', 1))
    maximum = int(math.ceil(total / page_limit))
    current_page = int(request.args.get('current_page', 1))
    pages = range(1, maximum + 1)

    recipes = mongo.db.recipes.find().limit(page_limit).skip(
        (current_page - 1)*page_limit)

    return render_template(
        'allrecipes.html',
        recipes=recipes,
        total=total,
        page_limit=page_limit,
        current_page=current_page,
        pages=pages,
        offset=offset,
        maximum=maximum,
        )
#READ: route to show each Editor's individual recipe by recipe_id
@app.route('/show_recipe/<recipe_id>', methods=['GET', 'POST'])
def show_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template(
        'recipe.html', recipe=the_recipe)

#READ: route to read all recipes under starter category
@app.route('/starter')
def starter():
         starter = mongo.db.recipes.find ({'categories': 'Starter'})
         return render_template('starter.html',
                           categories=starter)

#READ: route to read all recipes under main category
@app.route('/mains')
def mains():
         mains = mongo.db.recipes.find ({'categories': 'Main'})
         return render_template('mains.html',
                           categories=mains)

#READ: route to read all recipes under dessert category
@app.route('/desserts')
def desserts():
         desserts = mongo.db.recipes.find ({'categories': 'Dessert'})
         return render_template('desserts.html',
                           categories=desserts)

#READ: Route to display user's recipes saved in the account, querying using session - email
@app.route('/account', methods=['GET', 'POST'])
def account():
    user_account = session['email']
    query = ({'email': user_account})
    my_recipes = mongo.db.users_recipes.find(query)
    return render_template('account.html', recipes=my_recipes)

#READ: Route to show user's individual saved recipe
@app.route('/show_myrecipe/<account_id>', methods=['GET', 'POST'])
def show_myrecipe(account_id):
    my_recipe = mongo.db.users_recipes.find_one({'_id': ObjectId(account_id)})
    return render_template('myrecipes.html', recipe=my_recipe)

#UPDATE: Route to render edit form with recipe information from database
@app.route('/edit_myrecipe/<account_id>', methods=['GET', 'POST'])
def edit_myrecipe(account_id):
    edit = mongo.db.users_recipes.find_one({'_id': ObjectId(account_id)}) 
    return render_template('edit_myrecipe.html', recipe=edit)

#UPDATE: Route to update recipe information in the database
@app.route('/update_myrecipe/<account_id>', methods=['GET','POST'])
def update_myrecipe(account_id):
    users_recipes = mongo.db.users_recipes
    recipe = mongo.db.users_recipes.find_one({"_id": ObjectId(account_id)})
    users_recipes.update({"_id": ObjectId(account_id)},{
        "recipe_name": request.form.get("recipe_name"),
        "categories": request.form.get("categories"),
        "preparation_time": request.form.get("preparation_time"),
        "cooking_time": request.form.get("cooking_time"),
        "serving_portion": request.form.get("serving_portion"),
        "ingredients": request.form.get("ingredients").split('\r'),
        "methods": request.form.get("methods").split('\r'),
        "notes": request.form.get("notes"),
        "email":session["email"]
    })
    flash(f"Your recipe has been updated!")
    return redirect(url_for("account", recipe_id=account_id))
 
#DELETE - Route to delete user's recipe when Delete button is clicked.
@app.route('/delete_recipe/<account_id>', methods=['GET', 'POST'])
def delete_recipe(account_id):
    mongo.db.users_recipes.remove({'_id': ObjectId(account_id)})
    flash('Your recipe has been deleted!', 'warning')
    return redirect(url_for('account'))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('homepage'))    

if __name__ == '__main__':
    app.run (os.environ.get('IP', '0.0.0.0'),
            int(os.environ.get('PORT', '5000')),
            debug=True)
