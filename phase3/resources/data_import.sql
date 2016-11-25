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

-- COURSE
INSERT INTO course (courseNumber, name, instructorfName, instructorlName, designation, estNumberStudents) VALUES ('ARCH 4803', 'Green Infrastructure: EPA Campus Rainwater Challenge', 'Richard', 'Dagenhart', 'Sustainable Communities', '26');
INSERT INTO course (courseNumber, name, instructorfName, instructorlName, designation, estNumberStudents) VALUES ('BMED 2250', 'Problems in Biomedical Engineering', 'Barbara Burks', 'Fasse', 'Community', '300');
INSERT INTO course (courseNumber, name, instructorfName, instructorlName, designation, estNumberStudents) VALUES ('PUBP 3315', 'Environmental Policy and Politics', 'Alice', 'Favero', 'Sustainable Communities', '25');
INSERT INTO course (courseNumber, name, instructorfName, instructorlName, designation, estNumberStudents) VALUES ('EAS 2803', 'Urban Forest', 'Monica', 'Halka', 'Sustainable Communities', '10');
INSERT INTO course (courseNumber, name, instructorfName, instructorlName, designation, estNumberStudents) VALUES ('BIOL 1511', 'Honors Biological Principles; Honors Organismal Biology', 'Brian', 'Hammer', 'Sustainable Communities', '150');
INSERT INTO course (courseNumber, name, instructorfName, instructorlName, designation, estNumberStudents) VALUES ('EAS 1600', 'Introduction to Environmental Science', 'Dana', 'Hartley', 'Community', '600');
INSERT INTO course (courseNumber, name, instructorfName, instructorlName, designation, estNumberStudents) VALUES ('EAS 1601', 'Habitable Planet', 'Dana', 'Hartley', 'Community', '600');
INSERT INTO course (courseNumber, name, instructorfName, instructorlName, designation, estNumberStudents) VALUES ('EAS 2750', 'Physics of the Weather', 'Dana', 'Hartley', 'Community', '30');
INSERT INTO course (courseNumber, name, instructorfName, instructorlName, designation, estNumberStudents) VALUES ('EAS 1000', 'The Earth', 'Greg', 'Huey', 'Sustainable Communities', '26');
INSERT INTO course (courseNumber, name, instructorfName, instructorlName, designation, estNumberStudents) VALUES ('EAS 2000', 'The (Reverse) Sun', 'Harrison', 'Wells', 'Community', '300');
INSERT INTO course (courseNumber, name, instructorfName, instructorlName, designation, estNumberStudents) VALUES ('EAS 3000', 'Vibrations', 'Cisco', 'Ramon', 'Sustainable Communities', '52');
INSERT INTO course (courseNumber, name, instructorfName, instructorlName, designation, estNumberStudents) VALUES ('EAS 4000', 'The Speed Force', 'Barry', 'Allen', 'Sustainable Communities', '52');
INSERT INTO course (courseNumber, name, instructorfName, instructorlName, designation, estNumberStudents) VALUES ('BMED 1000', 'Healing', 'Oliver', 'Queen', 'Sustainable Communities', '150');
INSERT INTO course (courseNumber, name, instructorfName, instructorlName, designation, estNumberStudents) VALUES ('BMED 2000', 'Watching', 'Felicity', 'Smoak', 'Community', '600');
INSERT INTO course (courseNumber, name, instructorfName, instructorlName, designation, estNumberStudents) VALUES ('BMED 3000', 'Islands', 'Slade', 'Wilson', 'Community', '600');
INSERT INTO course (courseNumber, name, instructorfName, instructorlName, designation, estNumberStudents) VALUES ('BMED 4000', 'Alloys', 'Ray', 'Palmer', 'Community', '30');
INSERT INTO course (courseNumber, name, instructorfName, instructorlName, designation, estNumberStudents) VALUES ('CS 1301', 'Python', 'Jay', 'Summet', 'Sustainable Communities', '150');
INSERT INTO course (courseNumber, name, instructorfName, instructorlName, designation, estNumberStudents) VALUES ('CS 2200', 'Systems and Networks', 'Tom', 'Conte', 'Sustainable Communities', '151');
INSERT INTO course (courseNumber, name, instructorfName, instructorlName, designation, estNumberStudents) VALUES ('CS 3600', 'AI', 'Jim', 'Rehg', 'Sustainable Communities', '152');
INSERT INTO course (courseNumber, name, instructorfName, instructorlName, designation, estNumberStudents) VALUES ('CS 4400', 'Databases', 'Monica', 'Sweat', 'Sustainable Communities', '153');

-- COURSE CATEGORY
INSERT INTO course_category (courseNumber, categoryName) VALUES ('ARCH 4803', 'computing for good');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('ARCH 4803', 'doing good for your neighborhood');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('BMED 2250', 'computing for good');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('BMED 2250', 'doing good for your neighborhood');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('PUBP 3315', 'urban development');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('PUBP 3315', 'sustainable communities');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('EAS 2803', 'urban development');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('EAS 2803', 'sustainable communities');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('BIOL 1511', 'sustainable communities');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('EAS 1600', 'urban development');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('EAS 1600', 'sustainable communities');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('EAS 1601', 'urban development');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('EAS 1601', 'sustainable communities');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('EAS 2750', 'urban development');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('EAS 2750', 'sustainable communities');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('EAS 1000', 'urban development');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('EAS 1000', 'sustainable communities');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('EAS 2000', 'urban development');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('EAS 2000', 'sustainable communities');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('EAS 3000', 'urban development');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('EAS 3000', 'sustainable communities');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('EAS 4000', 'sustainable communities');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('BMED 1000', 'sustainable communities');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('BMED 2000', 'sustainable communities');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('BMED 3000', 'sustainable communities');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('BMED 4000', 'sustainable communities');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('CS 1301', 'computing for good');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('CS 2200', 'computing for good');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('CS 3600', 'computing for good');
INSERT INTO course_category (courseNumber, categoryName) VALUES ('CS 4400', 'computing for good');

-- PROJECT
INSERT INTO project (name, estNum, description, advfName, advlName, advEmail, desigName) VALUES ('Excel Peer Support Network', 60, 'Excel (www.excel.gatech.edu) is a four-year, dual certificate program for students with intellectual and developmental disabilities. The Peer Support Network is designed to provide the individualized support necessary for Excel students to thrive at Georgia Tech. ', 'Marnie', 'Williams', 'mwilliams@gatech.edu', 'Community');
INSERT INTO project (name, estNum, description, advfName, advlName, advEmail, desigName) VALUES ('ESW Hydroponics/Urban Farming Project', 7, 'The Hydroponics/Urban Farming Project experiments with different ways to grow produce in urban areas using limited space and water resources. We investigate both soil-based and hydroponic methods of growing in order to find the most efficient, economically viable, and environmentally sustainable way to grow produce in Atlanta. ', 'Nicole', 'Kinnard', 'nkinnard@gatech.edu', 'Sustainable Communities');
INSERT INTO project (name, estNum, description, advfName, advlName, advEmail, desigName) VALUES ('Excel Current Events', 15, 'Excel Current Events is a participation (not for credit) course for degree-seeking students who are interested in developing their communication skills in conversations with adults with intellectual and developmental disabilities. ', 'Ashley', 'Bidlack', 'abidlack@gatech.edu', 'Community');
INSERT INTO project (name, estNum, description, advfName, advlName, advEmail, desigName) VALUES ('Shakespeare in Prison Project', 20, 'As the world celebrates the 400th anniversary of Shakespeare’s death in 2016, Georgia Tech students will travel to a high-security men’s prison outside Atlanta to discuss Shakespeare with incarcerated students. ', 'Sarah', 'Higinbotham', 'shiginbotham@gatech.edu', 'Community');
INSERT INTO project (name, estNum, description, advfName, advlName, advEmail, desigName) VALUES ('Know Your Water Project', 10, 'This project will allow students to be part of a large, crowd-sourced study – at little cost to themselves – to contribute to a knowledge bank of how different communities treat and track their water quality. If you are interested in participating in this study, please let us know. ', 'Neha', 'Kumar', 'nkumar@gatech.edu', 'Sustainable Communities');
INSERT INTO project (name, estNum, description, advfName, advlName, advEmail, desigName) VALUES ('Epic Intentions', 20, 'Epic Intentions connects an interdisciplinary team of students with a local nonprofit to apply technical skills for social and civic good to help make the nonprofits make a greater impact in the community.', 'Yeji', 'Lee', 'ylee@gatech.edu', 'Community');
INSERT INTO project (name, estNum, description, advfName, advlName, advEmail, desigName) VALUES ('Acromantula', 60, 'Follow the spiders.', 'Rubeus', 'Hagrid', 'hagrid@gatech.edu', 'Community');
INSERT INTO project (name, estNum, description, advfName, advlName, advEmail, desigName) VALUES ('Basilisk', 7, 'Only the Heir of Slytherin can open the Chamber of Secrets', 'Tom', 'Riddle', 'voldemort@gatech.edu', 'Sustainable Communities');
INSERT INTO project (name, estNum, description, advfName, advlName, advEmail, desigName) VALUES ('Centaur', 15, 'This is where I leave you. You are safe now. Good luck, Harry Potter. The planets have been read wrongly before now, even by centaurs. I hope this is one of those times.', 'Firenze', 'Woodsman', 'centaur@gatech.edu', 'Community');
INSERT INTO project (name, estNum, description, advfName, advlName, advEmail, desigName) VALUES ('Dragon', 20, 'Accio Firebolt!', 'Hungarian', 'Horntail', 'dragon@gatech.edu', 'Community');
INSERT INTO project (name, estNum, description, advfName, advlName, advEmail, desigName) VALUES ('Ghoul', 10, 'In wizarding families the ghoul often becomes a talking point or even a family pet.', 'Ronald', 'Weasley', 'ghoul@gatech.edu', 'Sustainable Communities');
INSERT INTO project (name, estNum, description, advfName, advlName, advEmail, desigName) VALUES ('Leprechaun', 20, 'Leprechaun gold has the quality of disappearing after a few hours.', 'Ludo', 'Bagman', 'bagman@gatech.edu', 'Community');
INSERT INTO project (name, estNum, description, advfName, advlName, advEmail, desigName) VALUES ('Merperson', 60, 'Try opening it under the water.', 'Moaning', 'Myrtle', 'myrtle@gatech.edu', 'Community');
INSERT INTO project (name, estNum, description, advfName, advlName, advEmail, desigName) VALUES ('Three-headed Dog', 7, 'Guard the Philosophers Stone.', 'Fluffy', 'Guard', 'fluffy@gatech.edu', 'Sustainable Communities');
INSERT INTO project (name, estNum, description, advfName, advlName, advEmail, desigName) VALUES ('Toad', 15, 'Croak.', 'Trevor', 'Croak', 'trevor@gatech.edu', 'Community');
INSERT INTO project (name, estNum, description, advfName, advlName, advEmail, desigName) VALUES ('Troll', 20, 'Anyone can speak troll. All you have to do is point and grunt.', 'Point', 'Grunt', 'troll@gatech.edu', 'Community');
INSERT INTO project (name, estNum, description, advfName, advlName, advEmail, desigName) VALUES ('Thestral', 10, 'They can only be seen by people who have seen death.', 'Cedric', 'Diggory', 'cedric@gatech.edu', 'Sustainable Communities');
INSERT INTO project (name, estNum, description, advfName, advlName, advEmail, desigName) VALUES ('Hippogriff', 20, 'Buckbeak was a good hippogriff, always cleaned his feathers.', 'Buckbeak', 'Witherwings', 'buckbeak@gatech.edu', 'Community');
INSERT INTO project (name, estNum, description, advfName, advlName, advEmail, desigName) VALUES ('Owl', 10, 'Harry now carried a large cage that held a beautiful snowy owl, fast asleep with her head under her wing.', 'Hedwig', 'Snowy', 'hedwig@gatech.edu', 'Sustainable Communities');
INSERT INTO project (name, estNum, description, advfName, advlName, advEmail, desigName) VALUES ('Unicorn', 20, 'You have slain something pure and defenceless to save yourself, and you will have but a half-life, a cursed life, from the moment the blood touches your lips.', 'Quirinus ', 'Quirrell', 'unicorn@gatech.edu', 'Community');

-- PROJECT CATEGORY
INSERT INTO project_category (projectName, categoryName) VALUES ('Excel Peer Support Network', 'computing for good');
INSERT INTO project_category (projectName, categoryName) VALUES ('Excel Peer Support Network', 'doing good for your neighborhood');
INSERT INTO project_category (projectName, categoryName) VALUES ('Excel Peer Support Network', 'reciprocal teaching and learning');
INSERT INTO project_category (projectName, categoryName) VALUES ('ESW Hydroponics/Urban Farming Project', 'urban development');
INSERT INTO project_category (projectName, categoryName) VALUES ('ESW Hydroponics/Urban Farming Project', 'sustainable communities');
INSERT INTO project_category (projectName, categoryName) VALUES ('Excel Current Events', 'computing for good');
INSERT INTO project_category (projectName, categoryName) VALUES ('Excel Current Events', 'doing good for your neighborhood');
INSERT INTO project_category (projectName, categoryName) VALUES ('Excel Current Events', 'reciprocal teaching and learning');
INSERT INTO project_category (projectName, categoryName) VALUES ('Excel Current Events', 'technology for social good');
INSERT INTO project_category (projectName, categoryName) VALUES ('Shakespeare in Prison Project', 'urban development');
INSERT INTO project_category (projectName, categoryName) VALUES ('Shakespeare in Prison Project', 'sustainable communities');
INSERT INTO project_category (projectName, categoryName) VALUES ('Know Your Water Project', 'sustainable communities');
INSERT INTO project_category (projectName, categoryName) VALUES ('Know Your Water Project', 'crowd sourced');
INSERT INTO project_category (projectName, categoryName) VALUES ('Epic Intentions', 'doing good for your neighborhood');
INSERT INTO project_category (projectName, categoryName) VALUES ('Epic Intentions', 'collaborative action');
INSERT INTO project_category (projectName, categoryName) VALUES ('Acromantula', 'doing good for your neighborhood');
INSERT INTO project_category (projectName, categoryName) VALUES ('Acromantula', 'collaborative action');
INSERT INTO project_category (projectName, categoryName) VALUES ('Basilisk', 'sustainable communities');
INSERT INTO project_category (projectName, categoryName) VALUES ('Basilisk', 'crowd sourced');
INSERT INTO project_category (projectName, categoryName) VALUES ('Centaur', 'sustainable communities');
INSERT INTO project_category (projectName, categoryName) VALUES ('Centaur', 'crowd sourced');
INSERT INTO project_category (projectName, categoryName) VALUES ('Dragon', 'sustainable communities');
INSERT INTO project_category (projectName, categoryName) VALUES ('Dragon', 'crowd sourced');
INSERT INTO project_category (projectName, categoryName) VALUES ('Ghoul', 'sustainable communities');
INSERT INTO project_category (projectName, categoryName) VALUES ('Leprechaun', 'sustainable communities');
INSERT INTO project_category (projectName, categoryName) VALUES ('Merperson', 'sustainable communities');
INSERT INTO project_category (projectName, categoryName) VALUES ('Three-headed Dog', 'computing for good');
INSERT INTO project_category (projectName, categoryName) VALUES ('Toad', 'computing for good');
INSERT INTO project_category (projectName, categoryName) VALUES ('Troll', 'computing for good');
INSERT INTO project_category (projectName, categoryName) VALUES ('Thestral', 'computing for good');
INSERT INTO project_category (projectName, categoryName) VALUES ('Hippogriff', 'computing for good');
INSERT INTO project_category (projectName, categoryName) VALUES ('Owl', 'computing for good');
INSERT INTO project_category (projectName, categoryName) VALUES ('Unicorn', 'computing for good');
