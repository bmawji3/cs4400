from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField, RadioField
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
    new_major = SelectField('New Major')
    new_year = SelectField('New Year')

class SearchClassProject(FlaskForm):
    title = StringField('Title')
    designation = SelectField('Designation', default='')
    major = SelectField('Major', default='')
    year = SelectField('Year', default='')
    choice = RadioField(default='Both', choices=[('Project','Project'), ('Course','Course'), ('Both','Both')])

class AddProjectForm(FlaskForm):
    name = StringField('Project Name', [InputRequired()])
    advisorFName = StringField('Advisor First Name', [InputRequired()])
    advisorLName = StringField('Advisor Last Name', [InputRequired()])
    advisorEmail = StringField('Advisor Email', [InputRequired(), Email()])
    description = StringField('Description', [InputRequired()])
    designation = SelectField('Designation')
    majorRequirement = SelectField('Major Requirement')
    yearRequirement = SelectField('Year Requirement')
    deptRequirement = SelectField('Department Requirement')
    estNum = IntegerField('Estimated # of students', [InputRequired()])

class ProjectForm(FlaskForm):
    name = StringField('Name')

class AdminApplicationForm(FlaskForm):
    name = StringField('Name')

