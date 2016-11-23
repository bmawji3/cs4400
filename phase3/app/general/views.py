from app import app, mysql
from flask import render_template, redirect, flash, request, url_for, session, g
from flask_login import login_user, logout_user, current_user, login_required
from .forms import LoginForm, RegisterForm
from .models import User

cursor = mysql.connect().cursor()

@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        if session.get('role') == 'Student':
            return redirect(url_for('main_student'))
        else:
            return redirect(url_for('main_admin'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        query = 'SELECT username, userType FROM user WHERE username=\'{}\' AND password=\'{}\''.format(username, password)
        result = cursor.execute(query)
        if result:
            data = cursor.fetchone()
            flash('Access Granted :)')
            session['username'] = data[0]
            session['role'] = data[1]
            if data[1] == 'Student':
                return redirect(url_for('main_student'))
            else:
                return redirect(url_for('main_admin'))
    #         # user = User(username, password)
    #         # login_user(user)
        else:
            flash('DENIED!!')
    else:
        flash_errors(form)
    return render_template('login.html', title='Login', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    # if form.validate_on_submit():
    #     # print('user: {} \nemail: {} \npassword: {} \npassword_confirm: {}'.format(form.username.data, form.email.data, form.password.data, form.password_confirm.data))
    #     username = form.username.data
    #     password = form.password.data
    #     email = form.email.data
    #     ''' TODO fix query for correct table '''
    #     try:
    #         query = 'INSERT INTO user (username, password) VALUES (\'{}\',  \'{}\')'.format(username, password)
    #         cursor.execute(query)
    #     except:
    #         ''' TODO fix except clause for Integrity Error '''
    #         flash('User already exists in DB!!')
    # else:
    #     flash_errors(form)
    return render_template('register.html', title='Register', form=form)


@app.route('/main-student', methods=['GET', 'POST'])
def main_student():
    return render_template('student/main_student.html', title='Main')


@app.route('/main-admin', methods=['GET', 'POST'])
def main_admin():
    return render_template('admin/main_admin.html', title='Choose Functionality')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    session.pop('role', None)
#     logout_user()
    return redirect(url_for('login'))


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
