-- CREATE DATABASE colledge_db;

USE colledge_db;

CREATE TABLE IF NOT EXISTS departments(
    department_id INT NOT NULL AUTO_INCREMENT,
    department_name VARCHAR(100),
    PRIMARY KEY(department_id)
);

CREATE TABLE IF NOT EXISTS majors(
    major_id INT NOT NULL AUTO_INCREMENT,
    major_name VARCHAR(100),
    department_id INT,
    PRIMARY KEY(major_id),
    FOREIGN KEY(department_id) REFERENCES departments(department_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS students(
    student_id INT NOT NULL AUTO_INCREMENT,
    student_name VARCHAR(100),
    student_surname VARCHAR(100),
    start_of_study DATE NOT NULL,
    end_of_study DATE,
    department_id INT,
    major_id INT,
    PRIMARY KEY(student_id),
    FOREIGN KEY(department_id) REFERENCES departments(department_id) ON DELETE CASCADE,
    FOREIGN KEY(major_id) REFERENCES majors(major_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS teachers(
    teacher_id INT NOT NULL AUTO_INCREMENT,
    teacher_name VARCHAR(100),
    teacher_surname VARCHAR(100), 
    title VARCHAR(50),
    phone_number INT,
    department_id INT,
    PRIMARY KEY(teacher_id),
    FOREIGN KEY(department_id) REFERENCES departments(department_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS subjects(
    subject_id INT NOT NULL AUTO_INCREMENT,
    subject_name VARCHAR(100),
    subject_value INT,
    teacher_id INT,
    major_id INT,
    PRIMARY KEY(subject_id),
    FOREIGN KEY(teacher_id) REFERENCES teachers(teacher_id) ON DELETE CASCADE,
    FOREIGN KEY(major_id) REFERENCES majors(major_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS grades(
    grade_id INT NOT NULL AUTO_INCREMENT,
    grade_value VARCHAR(3),
    student_id INT,
    subject_id INT,
    teacher_id INT,
    PRIMARY KEY(grade_id),
    FOREIGN KEY(student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY(subject_id) REFERENCES subjects(subject_id) ON DELETE CASCADE,
    FOREIGN KEY(teacher_id) REFERENCES teachers(teacher_id) ON DELETE CASCADE
);