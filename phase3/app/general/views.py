from app import app, mysql
from flask import render_template, redirect, flash, request, url_for
from .forms import LoginForm, RegisterForm

cursor = mysql.connect().cursor()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', user="Admin")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # print('user: {} \npassword: {}'.format(form.username.data, form.password.data))
        # username = request.args.get('UserName')
        # password = request.args.get('Password')
        username = form.username.data
        password = form.password.data
        query = 'SELECT * FROM user WHERE username=\'{}\' AND password=\'{}\''.format(username, password)
        cursor.execute(query)
        data = cursor.fetchone()
        if (data):
            flash('Access Granted :)')
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

@app.route('/application_report', methods=['GET', 'POST'])
def view_applications():
    #try:
    #    query = 'SELECT' 
    #except:
    #    ''' TODO fix except clause for Integrity Error '''
    #    flash('User already exists in DB!!')
    return render_template('application_report.html', title='Application Report')

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))
