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
    get_categories = 'SELECT name FROM category ORDER BY name;'
    get_majors = 'SELECT majorName FROM major ORDER BY majorName;'
    get_desigs = 'SELECT name FROM designation ORDER BY name;'
    desig_list = []
    major_list = []
    year_list = [('', ''), ('Freshman', 'Freshman'), ('Sophmore', 'Sophmore'), ('Junior', 'Junior'), ('Senior', 'Senior')]
    category_html = ''
    table_html = ''
    # Setting the drop down values and adding default blank at the end of each list
    cursor.execute(get_categories)
    for item in cursor.fetchall():
        html = '<input type="checkbox" name="category" value="{}"> {}<br>\n\t\t\t'.format(item[0], item[0])
        category_html += html
    cursor.execute(get_majors)
    major_list.append(('',''))
    for item in cursor.fetchall():
        major_list.append((item[0], item[0]))
    cursor.execute(get_desigs)
    desig_list.append(('',''))
    for item in cursor.fetchall():
        desig_list.append((item[0], item[0]))
    form.designation.choices = desig_list
    form.major.choices = major_list
    form.year.choices = year_list
    # Searching
    if form.validate_on_submit():
        major = form.major.data
        dept = ''
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
            proj_query = "(select distinct name, 'Project' as type from project p "
            #Joins
            proj_query += "join project_category pc on p.name = pc.projectName "
            proj_query += "join project_requirements pr on pr.pName = p.name "
            #Conditionals
            proj_query += "where "
            #Category Conditional
            print(cat_result)
            proj_query += '('
            for i in range(len(cat_result) - 1):
                proj_query += 'pc.categoryName like \'{}%\' or '.format(cat_result[i])
            if len(cat_result) > 0:
                proj_query += 'pc.categoryName like \'{}%\' )'.format(cat_result[len(cat_result)-1])
            else:
                proj_query += 'pc.categoryName like \'%\' )'
            #Designation Conditional
            proj_query += 'and '
            proj_query += 'p.desigName like \'{}%\' '.format(designation)
            #Degree Conditional
            proj_query += 'and '
            proj_query += '((pr.pMajorRequirement like \'{}%\' or pr.pDeptRequirement like \'{}%\')'.format(major, dept)
            proj_query += ' or (pr.pMajorRequirement = \'none\' and pr.pDeptRequirement = \'none\')) '
            proj_query += 'and '
            proj_query += '(pr.pYearRequirement like \'%{}%\' or pr.pYearRequirement = \'none\') '.format(year)
            proj_query += 'and '
            proj_query += 'name like \'%{}%\' '.format(title)
            proj_query += ')'
        #Course Query - only if major and year are not specified
        course_query = ''
        if (project_or_course == 'Course' or project_or_course == 'Both') and (len(major) == 0 and len(year) == 0):
            course_query += "(select distinct name, 'Course' as type from course c "
            #Join
            course_query += "join course_category cc on c.courseNumber = cc.courseNumber "
            #Conditionals
            course_query += "where "
            #Category Conditional
            course_query += '('
            for i in range(len(cat_result) - 1):
                course_query += 'cc.categoryName like \'{}%\' or '.format(cat_result[i])
            if len(cat_result) > 0:
                course_query += 'cc.categoryName like \'{}%\' )'.format(cat_result[len(cat_result)-1])
            else:
                course_query += 'cc.categoryName like \'%\' )'
            #Designation Conditional
            course_query += 'and '
            course_query += 'c.designation like \'{}%\' '.format(designation)
            course_query += 'and '
            course_query += 'name like \'%{}%\' '.format(title)
            course_query += ')'
        search_query = ''
        if project_or_course == 'Both':
            if len(major) > 0 or len(year) > 0:
                search_query += proj_query
                search_query += 'order by name;'
            else:
                search_query += proj_query + ' union ' + course_query
                search_query += 'order by name;'
        elif project_or_course == 'Project':
            search_query += proj_query
            search_query += 'order by name;'
        else:
            if len(major) == 0 or len(year) == 0:
                search_query += course_query
                search_query += 'order by name;'
        print(search_query)
        if len(search_query) > 0:
            cursor.execute(search_query)
            for item in cursor.fetchall():
                # print(item)
                if item[1] == 'Course':
                    table_html += '<tr><td>{} <a class="btn btn-default" href="{}">View Course</a></td><td>{}</td></tr>'.format(item[0], url_for('course_student', course_name=item[0]), item[1])
                    print(item[0])
                else:
                    table_html += '<tr><td>{} <a class="btn btn-default" href="{}">View/Apply Project</a></td><td>{}</td></tr>'.format(item[0], url_for('project_student', project_name=item[0]), item[1])
    else:
        flash_errors(form)

    return render_template('student/main_student.html', title='Main', form=form, category_html=category_html, table_html=table_html)


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
    get_majors = 'SELECT majorName FROM major ORDER BY majorName;'
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
    table_html = ''
    query = 'SELECT date,projectName,status from applies_for where studentUsername = \'{}\''.format(session.get('username'))
    cursor.execute(query)
    for item in cursor.fetchall():
        table_html += '<tr><td>{}</td><td>{}</td><td>{}</td></tr>'.format(item[0],item[1],item[2])
    return render_template('student/my_application_student.html', title='My Application', table_html=table_html)


@app.route('/project-student/<path:project_name>', methods=['GET', 'POST'])
def project_student(project_name):
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
    query_requirements = 'SELECT pYearRequirement, pDeptRequirement, pMajorRequirement FROM project_requirements WHERE pName = \'{}\';'.format(project_name)
    cursor.execute(query_requirements)
    res_requirements = cursor.fetchall()

    pYearRequirement = res_requirements[0][0]
    pDeptRequirement = res_requirements[0][1]
    pMajorRequirement = res_requirements[0][2]

    hasRequirements = 0
    for requirement_tuple in res_requirements:
        for requirement in requirement_tuple:
            if requirement != 'none':
                requirements += requirement + '; ';
                hasRequirements = 1

    if hasRequirements:
        requirements = requirements[:-2]
    else:
        requirements = 'none'

    if form.validate_on_submit():
        username = session['username']
        query_application = 'SELECT status FROM applies_for WHERE studentUsername = \'{}\' AND projectName = \'{}\';'.format(username, project_name)
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
            satisfiesYearRequirement = 1
            satisfiesMajorRequirement = 0
            satisfiesDepartmentRequirement = 0

            if pMajorRequirement == 'none' and pDeptRequirement == 'none':
                satisfiesMajorRequirement = 1
                satisfiesDepartmentRequirement = 1

            if pYearRequirement != 'none':
                required_year = pYearRequirement[:pYearRequirement.index(' students')].lower()
                query_year = 'SELECT year FROM user WHERE username = \'{}\''.format(username)
                cursor.execute(query_year)
                if required_year == cursor.fetchall()[0][0].lower():
                    satisfiesYearRequirement = 1
                else:
                    satisfiesYearRequirement = 0

            if pMajorRequirement != 'none':
                required_major = pMajorRequirement[:pMajorRequirement.index(' students')].lower()
                query_major = 'SELECT majorName FROM user WHERE username = \'{}\''.format(username)
                cursor.execute(query_major)
                if required_major == cursor.fetchall()[0][0].lower():
                    satisfiesMajorRequirement = 1

            if pDeptRequirement != 'none':
                required_dept = pDeptRequirement[:pDeptRequirement.index(' students')].lower()
                query_dept = 'SELECT deptName FROM (SELECT user.username AS username, major.deptName AS deptName FROM user INNER JOIN major ON user.majorName = major.majorName) X WHERE username = \'{}\''.format(username)
                cursor.execute(query_dept)
                if required_dept == cursor.fetchall()[0][0].lower():
                    satisfiesDepartmentRequirement = 1

            if ((satisfiesMajorRequirement or satisfiesDepartmentRequirement) and satisfiesYearRequirement):
                query_apply = 'INSERT INTO applies_for(studentUsername, projectName, status) VALUES (\'{}\', \'{}\', \'{}\')'.format(username, project_name, "pending")
                cursor.execute(query_apply)
                conn.commit()
                flash('Thanks for applying! Your application has been received and will be reviewed in the next week.')
            else:
                flash('Sorry, you cannot apply because you don\'t meet the project\'s requirements.')
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


@app.route('/course-student/<path:course_name>', methods=['GET', 'POST'])
def course_student(course_name):
    # Check login & role -- DO NOT MODIFY
    if 'username' in session:
        if session.get('role') != 'Student':
            flash('You are not a Student!')
            return redirect(url_for('main_admin'))
    else:
        flash('You are not logged in!')
        return redirect(url_for('login'))
    # Code after this comment

    query_course_number = 'SELECT courseNumber FROM course WHERE name = \'{}\''.format(course_name)
    cursor.execute(query_course_number)

    course_number = cursor.fetchall()[0][0]
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
    fullTable = 'SELECT * from applies_for;'
    cursor.execute(fullTable)
    view_html = ''
    view_html += '<table>'
    view_html += '<tr> <th>Student Name</th><th>Project Name</th><th>Date</th><th>Status</th><th>Accept</th></tr>'
    for row in cursor.fetchall():
        view_html += '<tr>\n'
        for field in row:
            view_html += '<td>\t{}</td>\n'.format(field)
        view_html += '<td>'
        if row[3] == 'pending':
            view_html += '<button name = "Accept" onclick = "accept({})" class = "btn btn-success" id = "{}"> Accept </button> '.format(row[0]+"%"+row[1]+"%"+str(row[2])+"%"+row[3])
            view_html += '<button name = "Reject" onclick = "reject({})" class = "btn btn-danger" id = "{}"> Reject </button>'.format(row[0]+"%"+row[1]+"%"+str(row[2])+"%"+row[3])
        view_html += '</td>'
        view_html += '</tr>\n'
    view_html += '<table>'

    return render_template('admin/application_admin.html', title='View Applications', view_html = view_html)


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
    fullTable = 'SELECT projectName, count(projectName) from applies_for group by projectName;'
    cursor.execute(fullTable)
    view_html = ''
    view_html += '<table>'
    view_html += '<tr> <th>Project Name</th> <th>Applications</th></tr>'
    for row in cursor.fetchall():
        view_html += '<tr>\n'
        for field in row:
            view_html += '<td>\t{}</td>\n'.format(field)
        view_html += '</tr>\n'
    view_html += '<table>'

    return render_template('admin/pop_proj_admin.html', title='View Popular Projects', view_html = view_html)


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

    fullTable = 'select applies_for.projectName, (count(applies_for.projectName)), (final_count*100/count(applies_for.projectName)), popMajors from (select applies_for.projectName, substring_index(group_concat(majorName separator "/"), "/", 3) as popMajors from user,applies_for where applies_for.studentUsername = user.username group by projectName)sub, (select name, Sum(case when status is NULL then 0 else 1 END) as final_count from (select name, status from project left join (select projectName, status from applies_for where status = \'accepted\') X on name = X.projectName) Y group by name) accs, applies_for, user where user.username = applies_for.studentUsername and sub.projectName = applies_for.projectName and accs.name = applies_for.projectName group by applies_for.projectName;'
    #select applies_for.projectName, (count(applies_for.projectName)), (final_count*100/count(applies_for.projectName)), popMajors from (select applies_for.projectName, substring_index(group_concat(majorName separator "/"), "/", 3) as popMajors from user,applies_for where applies_for.studentUsername = user.username group by projectName)sub, (select name, Sum(case when status is NULL then 0 else 1 END) as final_count from (select name, status from project left join (select projectName, status from applies_for where status = 'accepted') X on name = X.projectName) Y group by name) accs, applies_for, user where user.username = applies_for.studentUsername and sub.projectName = applies_for.projectName and accs.name = applies_for.projectName group by applies_for.projectName;
    #(select name, Sum(case when status is NULL then 0 else 1 END) as final_count from (select name, status from project left join (select projectName, status from applies_for where status = 'accepted') X on name = X.projectName) Y group by name) accs
    cursor.execute(fullTable)
    view_html = ''
    view_html += '<table>'
    view_html += '<tr> <th>Project Name</th> <th># of Applicants</th><th>Acceptance Rate</th> <th>Top 3 Majors</th></tr>'
    for row in cursor.fetchall():
        view_html += '<tr>\n'
        for field in row:
            view_html += '<td>\t{}</td>\n'.format(field)
        view_html += '</tr>\n'
    view_html += '<table>'
    return render_template('admin/application_report_admin.html', title='View Application Report', view_html = view_html)


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
    get_majors = 'SELECT distinct majorName FROM major;'
    cursor.execute(get_majors)
    majorReqList = []
    for item in cursor.fetchall():
        majorReqList.append((item[0], item[0]))
    majorReqList.append(('none', 'none'))
    yearReqList = [('Freshman students only', 'Freshman students only'), ('Sophomore students only', 'Sophomore students only'), ('Junior students only', 'Junior students only'), ('Senior students only', 'Senior students only'), ('none', 'none')]
    deptReqList = [('College of Computing students only', 'College of Computing students only'), ('Ivan Allen College of Liberal Arts students only', 'Ivan Allen College of Liberal Arts students only'), ('Scheller School of Business students only', 'Scheller School of Business students only'), ('College of Design students only', 'College of Design students only'), ('College of Engineering students only', 'College of Engineering students only'), ('College of Science students only', 'College of Science students only'), ('none', 'none')]

    cursor.execute(get_designation)
    for item in cursor.fetchall():
        designation_list.append((item[0], item[0]))
    cursor.execute(get_category)
    for item in cursor.fetchall():
        html = '<input type="checkbox" name="category" value="{}"> {}<br>\n\t\t\t'.format(item[0], item[0])
        category_html += html
    form.designation.choices = designation_list
    form.yearRequirement.choices = yearReqList
    form.majorRequirement.choices = majorReqList
    form.deptRequirement.choices = deptReqList
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
        majorRequirements = form.majorRequirement.data
        yearRequirements = form.yearRequirement.data
        deptRequirements = form.deptRequirement.data
        estNum = form.estNum.data

        # queries
        check_query = 'SELECT name FROM project WHERE courseNumber=\'{}\''.format(name)
        result = cursor.execute(check_query)
        if not result:
            insert_query = 'INSERT INTO project (name, estNum, description, advisorFName, advisorLName, designation) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', {})'.format(name, estNum, description, advisorFName, advisorLName, designation)
            cursor.execute(insert_query)
            cursor.execute('INSERT INTO project_requirements (pName, pYearRequirement, pDeptRequirement, pMajorRequirement) VALUES (\'{}\', \'{}\', \'{}\', \'{}\')'.format(name, yearRequirements, deptRequirements, majorRequirements))
            for c in cat:
                insert_query_2 = 'INSERT INTO project_category (name, categoryName) VALUES (\'{}\', \'{}\')'.format(name, c)
                cursor.execute(insert_query_2)
            conn.commit()
            flash('Project has been added!')
            return redirect(url_for('add_project_admin'))
        else:
            flash('Conflict with Project Name!')
    else:
        flash_errors(form)
    return render_template('admin/add_project_admin.html', title='Add Project', form=form, category_html=category_html)


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
