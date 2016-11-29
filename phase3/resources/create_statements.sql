drop table if exists user;
drop table if exists project;
drop table if exists project_requirements;
drop table if exists department;
drop table if exists major;
drop table if exists designation;
drop table if exists category;
drop table if exists course;
drop table if exists applies_for;
drop table if exists course_category;
drop table if exists project_category;

CREATE TABLE user
(
    username    VARCHAR(60)     NOT NULL,
    password    VARCHAR(60)     NOT NULL,
    gtEmail     VARCHAR(60),
    year        VARCHAR(60),
    majorName   VARCHAR(60),
    userType    VARCHAR(10)     NOT NULL    DEFAULT "Student",
    PRIMARY KEY (username),
    FOREIGN KEY (majorName)     REFERENCES major(majorName),
    UNIQUE (gtEmail)
);

CREATE TABLE project
(
    name        VARCHAR(60)     NOT NULL,
    estNum      INT             NOT NULL,
    description VARCHAR(500)    NOT NULL,
    advfName    VARCHAR(60)     NOT NULL,
    advlName    VARCHAR(60)     NOT NULL,
    advEmail    VARCHAR(60)     NOT NULL,
    desigName   VARCHAR(60),
    PRIMARY KEY (name),
    FOREIGN KEY (desigName)     REFERENCES designation(name)
);

CREATE TABLE project_requirements
(
    pName           VARCHAR(60) NOT NULL,
    pRequirement    VARCHAR(60) NOT NULL,
    PRIMARY KEY (pName, pRequirement),
    FOREIGN KEY (pName)         REFERENCES project(name)
);

CREATE TABLE department
(
    deptName        VARCHAR(60) NOT NULL,
    PRIMARY KEY(deptName)
);

CREATE TABLE major
(
    majorName   VARCHAR(60)     NOT NULL,
    deptName    VARCHAR(60)     NOT NULL,
    PRIMARY KEY (majorName),
    FOREIGN KEY (deptName)      REFERENCES department(name)
);

CREATE TABLE designation
(
    name        VARCHAR(60)     NOT NULL,
    PRIMARY KEY (name)
);

CREATE TABLE category
(
    name        VARCHAR(60)     NOT NULL,
    PRIMARY KEY (name)
);

CREATE TABLE course
(
    courseNumber        VARCHAR(60)     NOT NULL,
    name                VARCHAR(60)     NOT NULL,
    instructorfName     VARCHAR(60)     NOT NULL,
    instructorlName     VARCHAR(60)     NOT NULL,
    designation         VARCHAR(60)     NOT NULL,
    estNumberStudents   INT             NOT NULL,
    PRIMARY KEY (courseNumber),
    UNIQUE (name),
    FOREIGN KEY (designation) REFERENCES designation(name)
);

CREATE TABLE applies_for
(
    studentUsername     VARCHAR(60)     NOT NULL,
    projectName         VARCHAR(60)     NOT NULL,
    date                TIMESTAMP       DEFAULT NOW(),
    status              VARCHAR(60)     NOT NULL,
    PRIMARY KEY (studentUsername, projectName),
    FOREIGN KEY (studentUsername)  REFERENCES user(username),
    FOREIGN KEY (projectName)   REFERENCES project(name)
);

CREATE TABLE project_category
(
    projectName     VARCHAR(60)     NOT NULL,
    categoryName    VARCHAR(60)     NOT NULL,
    PRIMARY KEY (projectName, categoryName),
    FOREIGN KEY (projectName)   REFERENCES project(name),
    FOREIGN KEY (categoryName)  REFERENCES category(name)
);

CREATE TABLE course_category
(
    courseNumber    VARCHAR(60)     NOT NULL,
    categoryName    VARCHAR(60)     NOT NULL,
    PRIMARY KEY (courseNumber, categoryName),
    FOREIGN KEY (courseNumber) REFERENCES course(courseNumber),
    FOREIGN KEY (categoryName) REFERENCES category(name)
);

ALTER TABLE `user` ENGINE = INNODB;
ALTER TABLE `project` ENGINE = INNODB;
ALTER TABLE `project_requirements` ENGINE = INNODB;
ALTER TABLE `department` ENGINE = INNODB;
ALTER TABLE `major` ENGINE = INNODB;
ALTER TABLE `designation` ENGINE = INNODB;
ALTER TABLE `category` ENGINE = INNODB;
ALTER TABLE `course` ENGINE = INNODB;
ALTER TABLE `applies_for` ENGINE = INNODB;
ALTER TABLE `course_category` ENGINE = INNODB;
ALTER TABLE `project_category` ENGINE = INNODB;