from app import app, mysql
from flask import render_template, redirect, flash, request, url_for, session, g
from flask_login import login_user, logout_user, current_user, login_required
from .forms import LoginForm, RegisterForm, CourseForm, EditProfileForm
from .models import User

conn = mysql.connect()
cursor = conn.cursor()

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
    if form.validate_on_submit():
        # data from form
        username = form.username.data
        password = form.password.data
        email = form.email.data
        # queries
        check_email = 'SELECT gtEmail FROM user WHERE gtEmail=\'{}\''.format(email)
        check_user = 'SELECT username FROM user WHERE username=\'{}\''.format(username)
        insert_query = 'INSERT INTO user (username, password, gtEmail) VALUES (\'{}\', \'{}\', \'{}\')'.format(username, password, email)
        loc = email.find('@gatech.edu')
        if loc == -1:
            flash('You must have an email address ending in \'@gatech.edu\'')
            return redirect(url_for('register'))
        # already checked '@gatech.edu'
        # now checking unique email
        check_em_result = cursor.execute(check_email)
        if not check_em_result:
            flash('Your email is unique!')
            # now checking unique username
            check_us_result = cursor.execute(check_user)
            if not check_us_result:
                flash('Your username is unique!')
                # enter info into db
                cursor.execute(insert_query)
                conn.commit()
                flash('Your info has been entered into the database!')
                return redirect(url_for('login'))
            else:
                flash('This username already exists in the database')
        else:
            flash('This email already exists in the database!')
    else:
        flash_errors(form)
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
    form = EditProfileForm()
    # Queries to fill drop down
    get_majors = 'SELECT majorName FROM major;'
    major_list = []
    dept = ''
    year_list = [('Freshman', 'Freshman'), ('Sophmore', 'Sophmore'), ('Junior', 'Junior'), ('Senior', 'Senior')]
    # Setting the drop down values
    cursor.execute(get_majors)
    for item in cursor.fetchall():
        major_list.append((item[0], item[0]))
    form.new_major.choices = major_list
    form.new_year.choices = year_list
    # Editing the profile
    if form.validate_on_submit():
        major = form.new_major.data
        year = form.new_year.data
        get_department = 'SELECT deptName from major where majorName = \'{}\''.format(major)
        cursor.execute(get_department)
        dept = cursor.fetchall()[0][0]
        print(dept[0][0])
        # queries
        update_query = 'UPDATE user SET majorName = \'{}\', year = \'{}\' WHERE username = \'{}\''.format(major, year, session.get('username'))
        print(update_query)
        cursor.execute(update_query)
        conn.commit()
    else:
        flash_errors(form)

    return render_template('student/edit_student.html', title='Edit Profile', form=form, dept=dept)


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
    form = CourseForm()
    # Queries to fill drop down
    get_designation = 'SELECT name FROM designation;'
    get_category = 'SELECT name FROM category;'
    designation_list = []
    category_html = ''
    # Setting the drop down values
    cursor.execute(get_designation)
    for item in cursor.fetchall():
        designation_list.append((item[0], item[0]))
    cursor.execute(get_category)
    for item in cursor.fetchall():
        # html = '<option value="{}">{}</option>'.format(item[0], item[0])
        html = '<input type="checkbox" name="category" value="{}"><br>\n'.format(item[0])
        category_html += html
    form.designation.choices = designation_list
    # Adding the course
    if form.validate_on_submit():
        cnum = form.courseNumber.data
        cname = form.courseName.data
        instructor_f = form.instructor_f.data
        instructor_l = form.instructor_l.data
        designation = form.designation.data
        enum = form.estNum.data
        # queries
        check_query = 'SELECT courseNumber, name FROM course WHERE courseNumber=\'{}\' OR name=\'{}\''.format(cnum, cname)
        result = cursor.execute(check_query)
        if not result:
            insert_query = 'INSERT INTO course (courseNumber, name, instructorfName, instructorlName, designation, estNumberStudents) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', {})'.format(cnum, cname, instructor_f, instructor_l, designation, enum)
            # print (insert_query)
            # insert_query_2 = 'INSERT INTO course_category (courseNumber, categoryName) VALUES (\'{}\', \'{}\')'.format(cnum, category)
            # print (insert_query_2)
        else:
            flash('Conflict with Course Number or Course Name!')
    else:
        flash_errors(form)
    return render_template('admin/add_course_admin.html', title='Add Course', form=form, category_html=category_html)


################# END ADMIN FUNCTIONS #################
cat = ''
@app.route('/test', methods=['GET', 'POST'])
def test():
    data = request.get_json()
    # global cat
    # cat = data['cats']
    # print(cat)
    return ''

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
