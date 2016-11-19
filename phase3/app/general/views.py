from app import app, mysql
from flask import render_template, redirect, flash, request, url_for, session, g
from flask_login import login_user, logout_user, current_user, login_required
from .forms import LoginForm, RegisterForm
from .models import User

cursor = mysql.connect().cursor()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', user="Admin")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        query = 'SELECT * FROM user WHERE username=\'{}\' AND password=\'{}\''.format(username, password)
        cursor.execute(query)
        data = cursor.fetchone()
        if (data):
            flash('Access Granted :)')
            # user = User(username, password)
            # login_user(user)
        else:
            flash('DENIED!!')
    else:
        flash_errors(form)
    return render_template('login.html', title='Login', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # print('user: {} \nemail: {} \npassword: {} \npassword_confirm: {}'.format(form.username.data, form.email.data, form.password.data, form.password_confirm.data))
        username = form.username.data
        password = form.password.data
        email = form.email.data
        ''' TODO fix query for correct table '''
        try:
            query = 'INSERT INTO user (username, password) VALUES (\'{}\',  \'{}\')'.format(username, password)
            cursor.execute(query)
        except:
            ''' TODO fix except clause for Integrity Error '''
            flash('User already exists in DB!!')
    else:
        flash_errors(form)
    return render_template('register.html', title='Register', form=form)


# @app.route('/logout', methods=['GET', 'POST'])
# def logout():
#     logout_user()
#     return redirect(url_for('index'))


# @app.before_request
# def before_request():
#     g.user = current_user


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))
