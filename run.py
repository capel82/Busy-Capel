import os
import math
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
#---- forms extension-flask WTF----#

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from forms import RegistrationForm, LoginForm
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


# ----- READ ALL RECIPES ----- #

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

@app.route('/show_recipe/<recipe_id>', methods=['GET', 'POST'])
def show_recipe(recipe_id):
 
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template(
        'recipe.html', recipe=the_recipe)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created successfully for {form.email.data}!', 'success')
        return redirect(url_for('register'))
    return render_template('register.html', title='register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('allrecipes'))
        else:
            flash('Login Unsuccessful. Please check email address and password', 'danger')
    return render_template('login.html', title='login', form=form)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(8000),
            debug=True)
