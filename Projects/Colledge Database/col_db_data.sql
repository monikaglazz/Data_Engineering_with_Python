-- Insert rows into departments table
INSERT INTO departments (department_name) VALUES 
    ('Computer Science'),
    ('Mathematics'),
    ('Biology'),
    ('English'),
    ('History');

-- Insert rows into majors table
INSERT INTO majors (major_name, department_id) VALUES 
    ('Computer Science', 1),
    ('Applied Mathematics', 2),
    ('Biology', 3),
    ('Linguistics', 4),
    ('History', 5);

-- Insert rows into students table
INSERT INTO students (student_name, student_surname, start_of_study, end_of_study, department_id, major_id) VALUES 
    ('John', 'Doe', '2020-09-01', '2024-06-01', 1, 1),
    ('Jane', 'Doe', '2020-09-01', '2024-06-01', 1, 1),
    ('Alice', 'Smith', '2021-09-01', '2025-06-01', 2, 2),
    ('Bob', 'Johnson', '2021-09-01', '2025-06-01', 2, 2),
    ('David', 'Lee', '2020-09-01', '2024-06-01', 1, 1);

-- Insert rows into teachers table
INSERT INTO teachers (teacher_name, teacher_surname, title, phone_number, department_id) VALUES 
    ('Michael', 'Brown', 'Assistant Professor', 1234567890, 1),
    ('Sarah', 'Davis', 'Associate Professor', 2345678901, 2),
    ('David', 'Miller', 'Professor', 3456789012, 1),
    ('Jennifer', 'Wilson', 'Assistant Professor', 4567890123, 3),
    ('Robert', 'Garcia', 'Associate Professor', 5678901234, 5);

-- Insert rows into subjects table
INSERT INTO subjects (subject_name, subject_value, teacher_id, major_id) VALUES 
    ('Data Structures', 90, 1, 1),
    ('Calculus I', 85, 2, 2),
    ('Biology 101', 80, 3, 3),
    ('Introduction to Linguistics', 95, 4, 4),
    ('World History', 88, 5, 5);

-- Insert rows into grades table
INSERT INTO grades (grade_value, student_id, subject_id, teacher_id) VALUES 
    ('A', 1, 1, 1),
    ('B', 2, 1, 1),
    ('B+', 3, 2, 2),
    ('A-', 4, 2, 2),
    ('A+', 5, 5, 5);
