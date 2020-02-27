import os

from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Cluster0'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template("index.html", recipes=mongo.db.recipes.find().limit(4))
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find().limit(3))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(8000),
            debug=True)
