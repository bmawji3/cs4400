from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', [InputRequired()])
    password = StringField('Password', [InputRequired()])

class RegisterForm(FlaskForm):
    username = StringField('Username', [InputRequired()])
    email = StringField('Email', [InputRequired()])
    password = StringField('Password', [InputRequired()])
    password_confirm = StringField('Confirm Password', [InputRequired(), EqualTo('password', message='Passwords must match')])