from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import InputRequired, EqualTo, Email

class LoginForm(FlaskForm):
    username = StringField('Username', [InputRequired()])
    password = StringField('Password', [InputRequired()])

class RegisterForm(FlaskForm):
    username = StringField('Username', [InputRequired()])
    email = StringField('Email', [InputRequired(), Email()])
    password = StringField('Password', [InputRequired()])
    password_confirm = StringField('Confirm Password', [InputRequired(), EqualTo('password', message='Passwords must match')])

class CourseForm(FlaskForm):
    courseNumber = StringField('Course Number', [InputRequired()])
    courseName = StringField('Course Name', [InputRequired()])
    instructor = StringField('Instructor', [InputRequired()])
    designation = SelectField('Designation')
    category = SelectField('Category')
    estNum = IntegerField('Estimated # of students', [InputRequired()])

