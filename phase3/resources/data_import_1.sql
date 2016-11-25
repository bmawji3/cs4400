-- CATEGORY
INSERT INTO category (name) VALUES ('computing for good');
INSERT INTO category (name) VALUES ('doing good for your neighborhood');
INSERT INTO category (name) VALUES ('reciprocal teaching and learning');
INSERT INTO category (name) VALUES ('urban development');
INSERT INTO category (name) VALUES ('adaptive learning');
INSERT INTO category (name) VALUES ('technology for social good');
INSERT INTO category (name) VALUES ('sustainable communities');
INSERT INTO category (name) VALUES ('crowd-sourced');
INSERT INTO category (name) VALUES ('collaborative action');

-- DESIGNATION
INSERT INTO designation (name) VALUES ('Sustainable Communities');
INSERT INTO designation (name) VALUES ('Community');

-- DEPARTMENT
INSERT INTO department (deptName) VALUES ('College of Computing');
INSERT INTO department (deptName) VALUES ('College of Design');
INSERT INTO department (deptName) VALUES ('College of Engineering');
INSERT INTO department (deptName) VALUES ('College of Sciences');
INSERT INTO department (deptName) VALUES ('Ivan Allen College of Liberal Arts');
INSERT INTO department (deptName) VALUES ('Scheller College of Business');

-- MAJOR

-- Computing
INSERT INTO major (majorName, deptName) VALUES ('Computational Media', 'College of Computing');
INSERT INTO major (majorName, deptName) VALUES ('Computer Science', 'College of Computing');

-- Design
INSERT INTO major (majorName, deptName) VALUES ('Architecture', 'College of Design');
INSERT INTO major (majorName, deptName) VALUES ('Industrial Design', 'College of Design');
INSERT INTO major (majorName, deptName) VALUES ('Music Technology', 'College of Design');

-- Engineering
INSERT INTO major (majorName, deptName) VALUES ('Aerospace Engineering', 'College of Engineering');
INSERT INTO major (majorName, deptName) VALUES ('Biomedical Engineering', 'College of Engineering');
INSERT INTO major (majorName, deptName) VALUES ('Chemical and Biomolecular Engineering', 'College of Engineering');
INSERT INTO major (majorName, deptName) VALUES ('Civil Engineering', 'College of Engineering');
INSERT INTO major (majorName, deptName) VALUES ('Computer Engineering', 'College of Engineering');
INSERT INTO major (majorName, deptName) VALUES ('Electrical Engineering', 'College of Engineering');
INSERT INTO major (majorName, deptName) VALUES ('Environmental Engineering', 'College of Engineering');
INSERT INTO major (majorName, deptName) VALUES ('Industrial Engineering', 'College of Engineering');
INSERT INTO major (majorName, deptName) VALUES ('Materials Science and Engineering', 'College of Engineering');
INSERT INTO major (majorName, deptName) VALUES ('Mechanical Engineering', 'College of Engineering');
INSERT INTO major (majorName, deptName) VALUES ('Nuclear and Radiological Engineering', 'College of Engineering');

-- Sciences
INSERT INTO major (majorName, deptName) VALUES ('Applied Mathematics', 'College of Sciences');
INSERT INTO major (majorName, deptName) VALUES ('Applied Physics', 'College of Sciences');
INSERT INTO major (majorName, deptName) VALUES ('Biochemistry', 'College of Sciences');
INSERT INTO major (majorName, deptName) VALUES ('Biology', 'College of Sciences');
INSERT INTO major (majorName, deptName) VALUES ('Chemistry', 'College of Sciences');
INSERT INTO major (majorName, deptName) VALUES ('Discrete Mathematics', 'College of Sciences');
INSERT INTO major (majorName, deptName) VALUES ('Earth and Atmospheric Sciences', 'College of Sciences');
INSERT INTO major (majorName, deptName) VALUES ('Physics', 'College of Sciences');
INSERT INTO major (majorName, deptName) VALUES ('Psychology', 'College of Sciences');

-- Liberal Arts
INSERT INTO major (majorName, deptName) VALUES ('Applied Language and Intercultural Studies', 'Ivan Allen College of Liberal Arts');
INSERT INTO major (majorName, deptName) VALUES ('Economics', 'Ivan Allen College of Liberal Arts');
INSERT INTO major (majorName, deptName) VALUES ('Economics and International Affairs', 'Ivan Allen College of Liberal Arts');
INSERT INTO major (majorName, deptName) VALUES ('Global Economics and Modern Languages', 'Ivan Allen College of Liberal Arts');
INSERT INTO major (majorName, deptName) VALUES ('History, Technology, and Society', 'Ivan Allen College of Liberal Arts');
INSERT INTO major (majorName, deptName) VALUES ('International Affairs', 'Ivan Allen College of Liberal Arts');
INSERT INTO major (majorName, deptName) VALUES ('International Affairs and Modern Languages', 'Ivan Allen College of Liberal Arts');
INSERT INTO major (majorName, deptName) VALUES ('Literature, Media, and Communication', 'Ivan Allen College of Liberal Arts');
INSERT INTO major (majorName, deptName) VALUES ('Public Policy', 'Ivan Allen College of Liberal Arts');

-- Business
INSERT INTO major (majorName, deptName) VALUES ('Business Administration', 'Scheller College of Business');

-- USER

-- Student
INSERT INTO user (username, password, gtEmail, year, majorName, userType) VALUES ('IAmGroot', 'IAmGroot', 'iamgroot@gatech.edu', 'Sophomore', 'Business Administration', 'Student');
INSERT INTO user (username, password, gtEmail, year, majorName, userType) VALUES ('Nick', 'Fury', 'eyepatch@gatech.edu', 'Sophomore', 'Public Policy', 'Student');
INSERT INTO user (username, password, gtEmail, year, majorName, userType) VALUES ('Peter', 'Parker', 'spiderman@gatech.edu', 'Sophomore', 'Chemistry', 'Student');
INSERT INTO user (username, password, gtEmail, year, majorName, userType) VALUES ('Bruce', 'Banner', 'hulk@gatech.edu', 'Sophomore', 'Physics', 'Student');
INSERT INTO user (username, password, gtEmail, year, majorName, userType) VALUES ('Bobbi', 'Morse', 'mockingbird@gatech.edu', 'Sophomore', 'Applied Mathematics', 'Student');
INSERT INTO user (username, password, gtEmail, year, majorName, userType) VALUES ('Steve', 'Rogers', 'captainamerica@gatech.edu', 'Junior', 'Computer Science', 'Student');
INSERT INTO user (username, password, gtEmail, year, majorName, userType) VALUES ('Tony', 'Stark', 'ironman@gatech.edu', 'Junior', 'Computer Science', 'Student');
INSERT INTO user (username, password, gtEmail, year, majorName, userType) VALUES ('Link', 'Zelda', 'lz@gatech.edu', 'Junior', 'Architecture', 'Student');
INSERT INTO user (username, password, gtEmail, year, majorName, userType) VALUES ('Walter', 'White', 'ww@gatech.edu', 'Junior', 'Chemical and Biomolecular Engineering', 'Student');
INSERT INTO user (username, password, gtEmail, year, majorName, userType) VALUES ('Samus', 'Aran', 'saran@gatech.edu', 'Junior', 'Computer Engineering', 'Student');
INSERT INTO user (username, password, gtEmail, year, majorName, userType) VALUES ('Stan', 'Lee', 'marvel@gatech.edu', 'Senior', 'Electrical Engineering', 'Student');
INSERT INTO user (username, password, gtEmail, year, majorName, userType) VALUES ('Dwight', 'Shrute', 'assistant-to-the-regional-manager@gatech.edu', 'Senior', 'Mechanical Engineering', 'Student');
INSERT INTO user (username, password, gtEmail, year, majorName, userType) VALUES ('Michael', 'Scott', 'number-one-boss@gatech.edu', 'Senior', 'Mechanical Engineering', 'Student');
INSERT INTO user (username, password, gtEmail, year, majorName, userType) VALUES ('Jim', 'Halpert', 'jhalpert@gatech.edu', 'Senior', 'Computer Science', 'Student');
INSERT INTO user (username, password, gtEmail, year, majorName, userType) VALUES ('Pam', 'Beasley', 'pbeasley@gatech.edu', 'Senior', 'Computer Science', 'Student');
INSERT INTO user (username, password, gtEmail, year, userType) VALUES ('Rabbit', 'trooper', 'rabbit@gatech.edu', 'Freshman', 'Student');
INSERT INTO user (username, password, gtEmail, year, userType) VALUES ('Thorny', 'trooper', 'thorny@gatech.edu', 'Freshman', 'Student');
INSERT INTO user (username, password, gtEmail, year, userType) VALUES ('Mac', 'trooper', 'mac@gatech.edu', 'Freshman', 'Student');
INSERT INTO user (username, password, gtEmail, year, userType) VALUES ('Farva', 'shenanigans', 'shenanigans@gatech.edu', 'Freshman', 'Student');
INSERT INTO user (username, password, gtEmail, year, userType) VALUES ('Foster', 'trooper', 'foster@gatech.edu', 'Freshman', 'Student');

-- Admin
INSERT INTO user (username, password, userType) VALUES ('normal', 'admin', 'Admin');
INSERT INTO user (username, password, userType) VALUES ('super', 'admin', 'Admin');
INSERT INTO user (username, password, userType) VALUES ('l33t', 'h4x0r', 'Admin');
INSERT INTO user (username, password, userType) VALUES ('s00p3r', 'l33t', 'Admin');
INSERT INTO user (username, password, userType) VALUES ('guess', 'mypassword', 'Admin');
