from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = StringField('Password')

class RegisterForm(FlaskForm):
    username = StringField('Username')
    email = StringField('Email')
    password = StringField('Password')
    password_confirm = StringField('Confirm Password', [InputRequired(), EqualTo('password', message='Passwords must match')])