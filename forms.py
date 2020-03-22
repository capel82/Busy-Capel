from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, Optional, EqualTo


class RegistrationForm(FlaskForm):
    email = StringField('Email Address',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class RecipesForm(FlaskForm):
    recipe_name = StringField ('Recipe Name',validators=[DataRequired()])
    categories= StringField ('Categories',validators=[DataRequired()])
    preparation_time = IntegerField ('Preparation Time (in minutes)',validators=[DataRequired()])
    cooking_time = IntegerField ('Cooking Time (in minutes)',validators=[DataRequired()])
    serving_portion = IntegerField ('Serving Portion',validators=[DataRequired()])
    ingredients = TextAreaField('Ingredients',validators=[DataRequired()])
    methods = TextAreaField ('Methods',validators=[DataRequired()])
    recipe_image = StringField ('recipe_image',validators=[Optional()])
    notes = TextAreaField ('Notes',validators=[Optional()])
    email = StringField('email',validators=[DataRequired(), Email()])
    submit = SubmitField ('Submit')

