-- DROP USER;
-- DROP project;
-- DROP project_requirements;
-- DROP department;
-- DROP major;
-- DROP designation;
-- DROP category;
-- DROP course;
-- DROP applies_for;
-- DROP course_category;
-- DROP project_category;

CREATE TABLE user
(
    username    VARCHAR(60)     NOT NULL,
    password    VARCHAR(60)     NOT NULL,
    gtEmail     VARCHAR(60),
    year        VARCHAR(60)    NOT NULL    DEFAULT "Freshman",
    majorName   VARCHAR(60),
    userType    VARCHAR(10),
    PRIMARY KEY (username),
    FOREIGN KEY (majorName)     REFERENCES major(majorName),
    UNIQUE (gtEmail)
);

CREATE TABLE project
(
    name        VARCHAR(60)     NOT NULL,
    estNum      INT             NOT NULL,
    description VARCHAR(140)    NOT NULL,
    advName     VARCHAR(60)     NOT NULL,
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
    name        VARCHAR(60) NOT NULL,
    PRIMARY KEY (name)
);

CREATE TABLE course
(
    courseNumber        VARCHAR(60)     NOT NULL,
    name                VARCHAR(60)     NOT NULL,
    instructor          VARCHAR(60)     NOT NULL,
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
    courseNumber    INT             NOT NULL,
    categoryName    VARCHAR(60)     NOT NULL,
    PRIMARY KEY (courseNumber, categoryName),
    FOREIGN KEY (courseNumber) REFERENCES course(courseNumber),
    FOREIGN KEY (categoryName) REFERENCES category(name)
);