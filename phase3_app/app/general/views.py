from app import app
from flask import render_template, redirect, flash
from .forms import LoginForm, RegisterForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', user="Admin")

@app.route('/reddit')
def reddit():
    # return render_template('reddit.html', title='reddit', user='Admin')
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('user: {} \npassword: {}'.format(form.username.data, form.password.data))
    return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print('user: {} \nemail: {} \npassword: {} \npassword_confirm: {}'.format(form.username.data, form.email.data, form.password.data, form.password_confirm.data))
    else:
        flash_errors(form)
    return render_template('register.html', form=form)

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))
