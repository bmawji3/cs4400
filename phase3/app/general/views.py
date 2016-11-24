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


################# BEGIN STUDENT FUNCTIONS #################
@app.route('/main-student', methods=['GET', 'POST'])
def main_student():
    # Check login & role -- DO NOT MODIFY
    if 'username' in session:
        if session.get('role') != 'Student':
            flash('You are not a Student!')
            return redirect(url_for('main_admin'))
    else:
        flash('You are not logged in!')
        return redirect(url_for('login'))
    # Code after this comment

    return render_template('student/main_student.html', title='Main')


@app.route('/me-student', methods=['GET', 'POST'])
def me_student():
    # Check login & role -- DO NOT MODIFY
    if 'username' in session:
        if session.get('role') != 'Student':
            flash('You are not a Student!')
            return redirect(url_for('main_admin'))
    else:
        flash('You are not logged in!')
        return redirect(url_for('login'))
    # Code after this comment

    return render_template('student/me_student.html', title='Me')


@app.route('/edit-student', methods=['GET', 'POST'])
def edit_student():
    # Check login & role -- DO NOT MODIFY
    if 'username' in session:
        if session.get('role') != 'Student':
            flash('You are not a Student!')
            return redirect(url_for('main_admin'))
    else:
        flash('You are not logged in!')
        return redirect(url_for('login'))
    # Code after this comment

    return render_template('student/edit_student.html', title='Edit Profile')


@app.route('/my-application-student', methods=['GET', 'POST'])
def my_application_student():
    # Check login & role -- DO NOT MODIFY
    if 'username' in session:
        if session.get('role') != 'Student':
            flash('You are not a Student!')
            return redirect(url_for('main_admin'))
    else:
        flash('You are not logged in!')
        return redirect(url_for('login'))
    # Code after this comment

    return render_template('student/my_application_student.html', title='My Application')


@app.route('/project-student', methods=['GET', 'POST'])
def project_student():
    # Check login & role -- DO NOT MODIFY
    if 'username' in session:
        if session.get('role') != 'Student':
            flash('You are not a Student!')
            return redirect(url_for('main_admin'))
    else:
        flash('You are not logged in!')
        return redirect(url_for('login'))
    # Code after this comment

    project = 'Know Your Water'
    return render_template('student/project_student.html', title='View and Apply Project', project=project)


@app.route('/course-student', methods=['GET', 'POST'])
def course_student():
    # Check login & role -- DO NOT MODIFY
    if 'username' in session:
        if session.get('role') != 'Student':
            flash('You are not a Student!')
            return redirect(url_for('main_admin'))
    else:
        flash('You are not logged in!')
        return redirect(url_for('login'))
    # Code after this comment

    course = 'CS/PSYC 3750'
    return render_template('student/course_student.html', title='View Course', course=course)


################# END STUDENT FUNCTIONS #################

################# BEGIN ADMIN FUNCTIONS #################
@app.route('/main-admin', methods=['GET', 'POST'])
def main_admin():
    # Check login & role -- DO NOT MODIFY
    if 'username' in session:
        if session.get('role') != 'Admin':
            flash('You are not a Admin!')
            return redirect(url_for('main_student'))
    else:
        flash('You are not logged in!')
        return redirect(url_for('login'))
    # Code after this comment

    return render_template('admin/main_admin.html', title='Choose Functionality')


@app.route('/application-admin', methods=['GET', 'POST'])
def application_admin():
    # Check login & role -- DO NOT MODIFY
    if 'username' in session:
        if session.get('role') != 'Admin':
            flash('You are not a Admin!')
            return redirect(url_for('main_student'))
    else:
        flash('You are not logged in!')
        return redirect(url_for('login'))
    # Code after this comment

    return render_template('admin/application_admin.html', title='View Applications')


@app.route('/pop-proj-admin', methods=['GET', 'POST'])
def pop_proj_admin():
    # Check login & role -- DO NOT MODIFY
    if 'username' in session:
        if session.get('role') != 'Admin':
            flash('You are not a Admin!')
            return redirect(url_for('main_student'))
    else:
        flash('You are not logged in!')
        return redirect(url_for('login'))
    # Code after this comment

    return render_template('admin/pop_proj_admin.html', title='View Popular Projects')


@app.route('/application-report-admin', methods=['GET', 'POST'])
def application_report_admin():
    # Check login & role -- DO NOT MODIFY
    if 'username' in session:
        if session.get('role') != 'Admin':
            flash('You are not a Admin!')
            return redirect(url_for('main_student'))
    else:
        flash('You are not logged in!')
        return redirect(url_for('login'))
    # Code after this comment

    return render_template('admin/application_report_admin.html', title='View Application Report')


@app.route('/add-project-admin', methods=['GET', 'POST'])
def add_project_admin():
    # Check login & role -- DO NOT MODIFY
    if 'username' in session:
        if session.get('role') != 'Admin':
            flash('You are not a Admin!')
            return redirect(url_for('main_student'))
    else:
        flash('You are not logged in!')
        return redirect(url_for('login'))
    # Code after this comment

    return render_template('admin/add_project_admin.html', title='Add Project')


@app.route('/add-course-admin', methods=['GET', 'POST'])
def add_course_admin():
    # Check login & role -- DO NOT MODIFY
    if 'username' in session:
        if session.get('role') != 'Admin':
            flash('You are not a Admin!')
            return redirect(url_for('main_student'))
    else:
        flash('You are not logged in!')
        return redirect(url_for('login'))
    # Code after this comment

    return render_template('admin/add_course_admin.html', title='Add Course')


################# END ADMIN FUNCTIONS #################

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
