from app import app, mysql
from flask import render_template, redirect, flash, request, url_for, session, g
from flask_login import login_user, logout_user, current_user, login_required
from .forms import LoginForm, RegisterForm, CourseForm, EditProfileForm, SearchClassProject, AddProjectForm, ProjectForm
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
    form = SearchClassProject()
    # Queries to fill drop down
    get_categories = 'SELECT name FROM category;'
    get_majors = 'SELECT majorName FROM major;'
    get_desigs = 'SELECT name FROM designation;'
    desig_list = []
    major_list = []
    year_list = [('', ''), ('Freshman', 'Freshman'), ('Sophmore', 'Sophmore'), ('Junior', 'Junior'), ('Senior', 'Senior')]
    category_html = ''
    # Setting the drop down values and adding default blank at the end of each list
    cursor.execute(get_categories)
    for item in cursor.fetchall():
        html = '<input type="checkbox" name="category" value="{}"> {}<br>\n\t\t\t'.format(item[0], item[0])
        category_html += html
    cursor.execute(get_majors)
    for item in cursor.fetchall():
        major_list.append((item[0], item[0]))
    major_list.append(('',''))
    cursor.execute(get_desigs)
    for item in cursor.fetchall():
        desig_list.append((item[0], item[0]))
    desig_list.append(('',''))
    form.designation.choices = desig_list
    form.major.choices = major_list
    form.year.choices = year_list
    # Searching
    if form.validate_on_submit():
        major = form.major.data
        dept_query = "select deptName from major where majorName = \'{}\'".format(major)
        cursor.execute(dept_query)
        if len(major) > 0:
            dept = cursor.fetchall()[0][0]
        title = form.title.data
        year = form.year.data
        designation = form.designation.data
        title_search = form.title.data
        project_or_course = form.choice.data
        #Project Query
        proj_query = ''
        if project_or_course == 'Project' or project_or_course == 'Both':
            proj_query = "(select name, 'Project' as type from project p "
            #Joins
            if len(cat_result) > 0:
                proj_query += "join project_category pc on p.name = pc.projectName "
            if len(major) > 0 or len(year) > 0:
                proj_query += "join project_requirements pr on pr.pName = p.name "
            #Conditionals
            if len(cat_result) > 0 or len(designation) > 0 or len(major) > 0 or len(year) > 0 or len(title) > 0:
                proj_query += "where "
                #Category Conditional
                if len(cat_result) > 0:
                    proj_query += '('
                    for i in range(len(cat_result) - 1):
                        proj_query += 'pc.categoryName = \'{}\' or '.format(cat_result[i])
                    proj_query += 'pc.categoryName = \'{}\' )'.format(cat_result[len(cat_result)-1])
                #Designation Conditional
                if len(designation) > 0:
                    if len(cat_result) > 0:
                        proj_query += 'and '
                    proj_query += 'p.desigName = \'{}\' '.format(designation)
                #Degree Conditional
                if len(major) > 0:
                    if len(designation) > 0 or len(cat_result):
                        proj_query += 'and '
                    req_major = ''
                    req_dept = ''
                    if major == 'Computer Science':
                        req_major = 'CS'
                        req_dept = 'COC'
                    elif dept == 'College of Design':
                        req_dept = 'COD'
                    else:
                        req_major = major
                        req_dept = dept
                    proj_query += '((pr.pMajorRequirement like \'%{}%\' or pr.pDeptRequirement like \'%{}%\')'.format(req_major, req_dept)
                    proj_query += ' or (pr.pMajorRequirement = \'none\' and pr.pDeptRequirement = \'none\')) '
                if len(year):
                    if len(major) > 0 or len(designation) > 0 or len(cat_result):
                        proj_query += 'and '
                    proj_query += '(pr.pYearRequirement like \'%{}%\' or pr.pYearRequirement = \'none\') '.format(year)
                if len(title):
                    if len(year) > 0 or len(major) > 0 or len(designation) > 0 or len(cat_result):
                        proj_query += 'and '
                    proj_query += 'name like \'%{}%\' '.format(title)
            proj_query += ')'
        #Course Query
        course_query = ''
        if project_or_course == 'Course' or project_or_course == 'Both':
            course_query += "(select name, 'Course' as type from course c "
            #Join
            if len(cat_result) > 0:
                course_query += "join course_category cc on c.courseNumber = cc.courseNumber "
            #Conditionals - only if major and year are not specified
            if len(major) == 0 and len(year) == 0:
                if len(designation) > 0 or len(cat_result) > 0 or len(title) > 0:
                    course_query += "where "
                    #Category Conditional
                    if len(cat_result) > 0:
                        course_query += '('
                        for i in range(len(cat_result) - 1):
                            course_query += 'cc.categoryName = \'{}\' or '.format(cat_result[i])
                        course_query += 'cc.categoryName = \'{}\' )'.format(cat_result[len(cat_result)-1])
                    #Designation Conditional
                    if len(designation) > 0:
                        if len(cat_result) > 0:
                            course_query += 'and '
                        course_query += 'c.designation = \'{}\' '.format(designation)
                    if len(title):
                        if len(designation) > 0:
                            course_query += 'and '
                        course_query += 'name like \'%{}%\' '.format(title)
            course_query += ')'
        search_query = ''
        if project_or_course == 'Both':
            search_query += proj_query + ' union ' + course_query
        elif project_or_course == 'Project':
            search_query += proj_query
        else:
            search_query += course_query
        search_query += 'order by name;'
        print(search_query)
    else:
        flash_errors(form)

    return render_template('student/main_student.html', title='Main', form=form, category_html=category_html)


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
    dept = 'N/A'
    # Editing the profile
    if form.validate_on_submit():
        # check that length of cat_result > 0
        major = form.new_major.data
        year = form.new_year.data
        get_department = 'SELECT deptName from major where majorName = \'{}\''.format(major)
        cursor.execute(get_department)
        dept = cursor.fetchall()[0][0]
        # queries
        update_query = 'UPDATE user SET majorName = \'{}\', year = \'{}\' WHERE username = \'{}\''.format(major, year, session.get('username'))
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
    form = ProjectForm()

    project_name = 'Thestral'
    query_project = 'SELECT estNum, description, advfName, advlName, advEmail, desigName FROM project WHERE name=\'{}\';'.format(project_name)
    cursor.execute(query_project)
    res_project = cursor.fetchall()

    estNum = res_project[0][0]
    description = res_project[0][1]
    advfName = res_project[0][2]
    advlName = res_project[0][3]
    advEmail = res_project[0][4]
    desigName = res_project[0][5]

    categories = ''
    query_categories = 'SELECT categoryName FROM project_category WHERE projectName = \'{}\';'.format(project_name)
    cursor.execute(query_categories)
    res_categories = cursor.fetchall()

    hasCategories = 0
    for category in res_categories:
        categories += category[0] + ', ';
        hasCategories = 1

    if hasCategories:
        categories = categories[:-2]

    requirements = ''
    query_requirements = 'SELECT pRequirement FROM project_requirements WHERE pName = \'{}\';'.format(project_name)
    cursor.execute(query_requirements)
    res_requirements = cursor.fetchall()

    hasRequirements = 0
    for requirement in res_requirements:
        requirements += requirement[0] + '; ';
        hasRequirements = 1

    if hasRequirements:
        requirements = requirements[:-2]

    if form.validate_on_submit():
        student_username = session['username']
        query_application = 'SELECT status FROM applies_for WHERE studentUsername = \'{}\' AND projectName = \'{}\';'.format(student_username, project_name)
        cursor.execute(query_application)
        if cursor.rowcount:
            status = cursor.fetchall()[0][0]
            if status == 'accepted':
                flash('You\'ve already been accepted!')
            elif status == 'rejected':
                flash('Sorry, you\'ve been rejected -- you cannot apply again.')
            elif status == 'pending':
                flash('Your application is pending -- hang tight!')
        else:
            flash('in progress')
        #print(session['username'])
    else:
        flash_errors(form)

    return render_template('student/project_student.html',
        title='View and Apply Project',
        project_name=project_name,
        estNum=estNum,
        description=description,
        advfName=advfName,
        advlName=advlName,
        advEmail=advEmail,
        desigName=desigName,
        categories=categories,
        requirements=requirements,
        form=form)


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

    course_number = 'CS 3600'
    query_course = 'SELECT name, instructorfName, instructorlName, designation, estNumberStudents FROM course WHERE courseNumber = \'{}\';'.format(course_number)
    cursor.execute(query_course)
    res_course = cursor.fetchall()

    course_name = res_course[0][0]
    instructorfName = res_course[0][1]
    instructorlName = res_course[0][2]
    designation = res_course[0][3]
    estNumberStudents = res_course[0][4]

    categories = ''
    query_categories = 'SELECT categoryName FROM course_category WHERE courseNumber = \'{}\';'.format(course_number)
    cursor.execute(query_categories)
    res_categories = cursor.fetchall()

    hasCategories = 0
    for category in res_categories:
        categories += category[0] + ', ';
        hasCategories = 1

    if hasCategories:
        categories = categories[:-2]

    return render_template('student/course_student.html',
        title='View Course',
        course_number=course_number,
        course_name=course_name,
        instructorfName=instructorfName,
        instructorlName=instructorlName,
        designation=designation,
        categories=categories,
        estNumberStudents=estNumberStudents)


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
    displayedStuff = 'SELECT * from applies_for;'
    cursor.execute(displayedStuff)
    html = '<p1>Insert table here</p1>'
    #for item in cursor.fetchall():
    #    html = '<\n>'
    #    #'<input type="checkbox" name="category" value="{}"> {}<br>\n\t\t\t'.format(item[0], item[0])
    #    view_html += html
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
    form = AddProjectForm()
    get_designation = 'SELECT name FROM designation;'
    get_category = 'SELECT name FROM category;'
    designation_list = []
    category_html = ''
    requirement_list = []
    cursor.execute(get_designation)
    for item in cursor.fetchall():
        designation_list.append((item[0], item[0]))
    cursor.execute(get_category)
    for item in cursor.fetchall():
        html = '<input type="checkbox" name="category" value="{}"> {}<br>\n\t\t\t'.format(item[0], item[0])
        category_html += html
    cursor.execute('SELECT * from project_requirements;')
    for item in cursor.fetchall():
        requirement_list.append(item[0])
    form.designation.choices = designation_list
    form.requirements.choices = requirement_list
    if form.validate_on_submit():
        if tnum == 0:
            flash('Error in the Category field - This field is required.')
            return redirect(url_for('add_course_admin'))
        name = form.name.data
        advisorFName = form.advisorFName.data
        advisorLName = form.advisorLName.data
        advisorEmail = form.advisorEmail.data
        description = form.description.data
        designation = form.designation.data
        requirements = form.requirements.data
        estNum = form.estNum.data
        # queries
        check_query = 'SELECT name FROM project WHERE courseNumber=\'{}\''.format(name)
        result = cursor.execute(check_query)
        if not result:
            insert_query = 'INSERT INTO project (name, estNum, description, advisorFName, advisorLName, designation) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', {})'.format(cnum, cname, instructor_f, instructor_l, designation, enum)
            cursor.execute(insert_query)
            for c in cat:
                insert_query_2 = 'INSERT INTO project_category (name, categoryName) VALUES (\'{}\', \'{}\')'.format(cnum, c)
                cursor.execute(insert_query_2)
            conn.commit()
            flash('Course has been inserted!')
            return redirect(url_for('add_course_admin'))
        else:
            flash('Conflict with Course Number or Course Name!')
    else:
        flash_errors(form)
    return render_template('admin/add_project_admin.html', title='Add Project', form=form)


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
        html = '<input type="checkbox" name="category" value="{}"> {}<br>\n\t\t\t'.format(item[0], item[0])
        category_html += html
    form.designation.choices = designation_list
    # Adding the course
    if form.validate_on_submit():
        if tnum == 0:
            flash('Error in the Category field - This field is required.')
            return redirect(url_for('add_course_admin'))
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
            insert_query = 'INSERT INTO course (courseNumber, name, instructorfName, instructorlName, designation, estNumberStudents) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', {})'.format(courseNumber, name, instructorfName, instructorlName, designation, estNumberStudents)
            cursor.execute(insert_query)
            for c in cat:
                insert_query_2 = 'INSERT INTO course_category (courseNumber, categoryName) VALUES (\'{}\', \'{}\')'.format(cnum, c)
                cursor.execute(insert_query_2)
            conn.commit()
            flash('Course has been inserted!')
            return redirect(url_for('add_course_admin'))
        else:
            flash('Conflict with Course Number or Course Name!')
    else:
        flash_errors(form)
    return render_template('admin/add_course_admin.html', title='Add Course', form=form, category_html=category_html)


################# END ADMIN FUNCTIONS #################
cat = ''
tnum = 0
@app.route('/test', methods=['GET', 'POST'])
def test():
    data = request.get_json()
    global cat
    cat = data['cats']
    global tnum
    tnum = data['nums']
    return ''

cat_result = ''
@app.route('/test_search', methods=['GET', 'POST'])
def test_search():
    data = request.get_json()
    # print("Data:",data)
    global cat_result
    cat_result = data['cat_results']
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
