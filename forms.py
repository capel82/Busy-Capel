from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField,TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo


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
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RecipesForm(FlaskForm):
    recipe_name = StringField ('Recipe Name',validators=[DataRequired()])
    categories= StringField ('Categories',validators=[DataRequired()])
    preparation_time = IntegerField ('Preparation Time',validators=[DataRequired()])
    cooking_time = IntegerField ('Cooking Time',validators=[DataRequired()])
    ingredients = TextAreaField ('Preparation Time',validators=[DataRequired()])
    methods = TextAreaField ('Preparation Time',validators=[DataRequired()])

    submit = SubmitField ('Add Recipe')

