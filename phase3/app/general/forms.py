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
    instructor_f = StringField('Instructor First Name', [InputRequired()])
    instructor_l = StringField('Instructor Last Name', [InputRequired()])
    designation = SelectField('Designation')
    # category = SelectField('Category')
    estNum = IntegerField('Estimated # of students', [InputRequired()])

class EditProfileForm(FlaskForm):
    new_major = SelectField('Major')
    new_year = SelectField('Year')

class AddProjectForm(FlaskForm):
    name = StringField('Project Name', [InputRequired()])
    advisor = StringField('Advisor', [InputRequired()])
    advisorEmail = StringField('Advisor Email', [InputRequired()])
    description = StringField('Description', [InputRequired()])
    designation = SelectField('Designation')
    estNum = IntegerField('Estimated # of students', [InputRequired()])
