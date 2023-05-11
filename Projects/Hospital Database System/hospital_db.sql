-- CREATE DATABASE hospital_db;

USE hospital_db;

-- create wing_name TABLE
CREATE TABLE IF NOT EXISTS wing_name(
    wing_id INT NOT NULL AUTO_INCREMENT,
    wing_name VARCHAR(100) NOT NULL UNIQUE,
    PRIMARY KEY(wing_id)
)AUTO_INCREMENT = 1;

-- create department table
CREATE TABLE IF NOT EXISTS department(
    department_id INT NOT NULL AUTO_INCREMENT,
    department_name VARCHAR(100) NOT NULL UNIQUE,
    floor_number INT NOT NULL,
    wing_id INT NOT NULL,
    PRIMARY KEY(department_id),
    FOREIGN KEY(wing_id) REFERENCES wing_name(wing_id) ON DELETE CASCADE
) AUTO_INCREMENT = 1;


-- create workers_type table
CREATE TABLE IF NOT EXISTS workers_type(
    type_id INT NOT NULL AUTO_INCREMENT,
    type_name VARCHAR(100) NOT NULL UNIQUE,
    PRIMARY KEY(type_id)
)AUTO_INCREMENT = 1;


-- create workers_responsibilities table
CREATE TABLE IF NOT EXISTS responsibilities(
    function_id INT NOT NULL AUTO_INCREMENT,
    function_name VARCHAR(100) NOT NULL UNIQUE,
    PRIMARY KEY(function_id)
)AUTO_INCREMENT = 1;


-- create countries table
CREATE TABLE IF NOT EXISTS countries(
    country_id INT NOT NULL AUTO_INCREMENT,
    country_name VARCHAR(100) NOT NULL UNIQUE,
    PRIMARY KEY(country_id)
)AUTO_INCREMENT = 1;


-- create cities table
CREATE TABLE IF NOT EXISTS cities(
    city_id INT NOT NULL AUTO_INCREMENT,
    city_name VARCHAR(100) NOT NULL UNIQUE,
    country_id INT NOT NULL,
    PRIMARY KEY(city_id), 
    FOREIGN KEY(country_id) REFERENCES countries(country_id) ON DELETE CASCADE
)AUTO_INCREMENT = 1;


-- create workers_address table
CREATE TABLE workers_address(
    address_id INT NOT NULL AUTO_INCREMENT,
    address VARCHAR(100) NOT NULL UNIQUE,
    city_id INT NOT NULL,
    PRIMARY KEY(address_id),
    FOREIGN KEY(city_id) REFERENCES cities(city_id) ON DELETE CASCADE
)AUTO_INCREMENT = 1;


CREATE TABLE specializations(
    specialization_id INT NOT NULL AUTO_INCREMENT,
    specjalization_name VARCHAR(100) NOT NULL UNIQUE,
    PRIMARY KEY(specialization_id)
)AUTO_INCREMENT = 1;

-- create workers table
CREATE TABLE workers(
    worker_id INT NOT NULL AUTO_INCREMENT,
    worker_type INT NOT NULL,
    worker_department INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    address INT NOT NULL,
    specialization INT NOT NULL,
    contract_start DATE NOT NULL,
    contract_end DATE,
    salary INT NOT NULL,
    PRIMARY KEY(worker_id),
    FOREIGN KEY(worker_type) REFERENCES workers_type(type_id) ON DELETE CASCADE,
    FOREIGN KEY(worker_department) REFERENCES department(department_id) ON DELETE CASCADE,
    FOREIGN KEY(address) REFERENCES workers_address(address_id) ON DELETE CASCADE,
    FOREIGN KEY(specialization) REFERENCES specializations(specialization_id) ON DELETE CASCADE
)AUTO_INCREMENT = 1;

-- create workers_responsibilities table
CREATE TABLE workers_responsibilities(
    res_id INT NOT NULL AUTO_INCREMENT,
    worker_id INT NOT NULL,
    function_id INT NOT NULL,
    PRIMARY KEY(res_id),
    FOREIGN KEY(worker_id) REFERENCES workers(worker_id) ON DELETE CASCADE,
    FOREIGN KEY(function_id) REFERENCES responsibilities(function_id) ON DELETE CASCADE
)AUTO_INCREMENT = 1;

-- create patients_address table
CREATE TABLE IF NOT EXISTS patients_address(
    address_id INT NOT NULL AUTO_INCREMENT,
    address VARCHAR(100) NOT NULL UNIQUE,
    city_id INT NOT NULL,
    PRIMARY KEY(address_id),
    FOREIGN KEY(city_id) REFERENCES cities(city_id) ON DELETE CASCADE
)AUTO_INCREMENT = 1;

CREATE TABLE genders(
    gender_id INT NOT NULL,
    gender_name VARCHAR(20) NOT NULL,
    PRIMARY KEY(gender_id)
)AUTO_INCREMENT = 1;

CREATE TABLE blood_types(
    blood_id INT NOT NULL,
    type VARCHAR(5) NOT NULL,
    PRIMARY KEY(blood_id)
)AUTO_INCREMENT = 1;

-- create patients table
CREATE TABLE IF NOT EXISTS patients(
    patient_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL,
    gender INT NOT NULL,
    address_id INT,
    phone INT(9) NOT NULL,
    email VARCHAR(50),
    blood_type INT NOT NULL,
    PRIMARY KEY(patient_id),
    FOREIGN KEY(gender) REFERENCES genders(gender_id) ON DELETE CASCADE,
    FOREIGN KEY(address_id) REFERENCES patients_address(address_id) ON DELETE CASCADE,
    FOREIGN KEY(blood_type) REFERENCES blood_types(blood_id) ON DELETE CASCADE
)AUTO_INCREMENT = 1;


-- create medicines table
CREATE TABLE IF NOT EXISTS medications(
    medication_id INT NOT NULL AUTO_INCREMENT,
    medication_name VARCHAR(100) NOT NULL UNIQUE,
    description VARCHAR(200) NOT NULL,
    purpose VARCHAR(50) NOT NULL,
    PRIMARY KEY (medication_id)
)AUTO_INCREMENT = 1;


-- create surgeries table
CREATE TABLE IF NOT EXISTS surgeries(
    surgery_id INT NOT NULL AUTO_INCREMENT,
    surgery_name VARCHAR(50) UNIQUE,
    PRIMARY KEY(surgery_id)
)AUTO_INCREMENT = 1;


-- create examinations table
CREATE TABLE IF NOT EXISTS examinations(
    examination_id INT NOT NULL AUTO_INCREMENT,
    examination_name VARCHAR(100) NOT NULL UNIQUE,
    PRIMARY KEY(examination_id)
)AUTO_INCREMENT = 1;


-- create patient_medicines table
CREATE TABLE IF NOT EXISTS patient_medications(
    patient_id INT NOT NULL,
    medication_id INT NOT NULL,
    PRIMARY KEY (patient_id, medication_id),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (medication_id) REFERENCES medications(medication_id) ON DELETE CASCADE
)AUTO_INCREMENT = 1;


-- create patient_surgeries table
CREATE TABLE IF NOT EXISTS patient_surgeries(
    patient_id INT NOT NULL,
    surgery_id INT NOT NULL,
    surgery_date DATE,
    main_surgeon INT NOT NULL,
    assisting_surgeon INT,
    PRIMARY KEY (patient_id, surgery_id),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (surgery_id) REFERENCES surgeries(surgery_id) ON DELETE CASCADE,
    FOREIGN KEY (main_surgeon) REFERENCES workers(worker_id) ON DELETE CASCADE,
    FOREIGN KEY (assisting_surgeon) REFERENCES workers(worker_id) ON DELETE CASCADE
)AUTO_INCREMENT = 1;

-- create examination_time_minute table
CREATE TABLE time_minute(
    minute_id INT NOT NULL,
    minute_value INT(2) NOT NULL,
    PRIMARY KEY(minute_id)
)AUTO_INCREMENT = 1;


-- create time table
CREATE TABLE IF NOT EXISTS time(
    time_id INT NOT NULL AUTO_INCREMENT,
    hour INT(2) NOT NULL UNIQUE,
    minute INT NOT NULL,
    PRIMARY KEY(time_id),
    FOREIGN KEY(minute) REFERENCES time_minute(minute_id) ON DELETE CASCADE
)AUTO_INCREMENT = 1;


-- create date_year table
CREATE TABLE IF NOT EXISTS date_year(
    year_id INT NOT NULL AUTO_INCREMENT,
    year_value INT(4) NOT NULL UNIQUE,
    PRIMARY KEY(year_id)
)AUTO_INCREMENT = 1;


-- create date_month table
CREATE TABLE IF NOT EXISTS date_month(
    month_id INT NOT NULL AUTO_INCREMENT,
    month_value INT(2) NOT NULL UNIQUE,
    year_id INT NOT NULL,
    PRIMARY KEY(month_id),
    FOREIGN KEY(year_id) REFERENCES date_year(year_id) ON DELETE CASCADE
)AUTO_INCREMENT = 1;

-- create date table
CREATE TABLE IF NOT EXISTS date(
    date_id INT NOT NULL AUTO_INCREMENT,
    day_value INT(2) NOT NULL UNIQUE,
    month_id INT NOT NULL,
    PRIMARY KEY(date_id),
    FOREIGN KEY(month_id) REFERENCES date_month(month_id) ON DELETE CASCADE
)AUTO_INCREMENT = 1;


-- create patient_examinations table
CREATE TABLE IF NOT EXISTS patient_examinations(
    patient_id INT NOT NULL,
    examination_id INT NOT NULL,
    examination_date INT NOT NULL,
    examination_time INT NOT NULL,
    examinator INT NOT NULL,
    examination_description VARCHAR(500) NOT NULL,
    PRIMARY KEY (patient_id, examination_id),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (examination_id) REFERENCES examinations(examination_id) ON DELETE CASCADE,
    FOREIGN KEY (examination_date) REFERENCES date(date_id) ON DELETE CASCADE,
    FOREIGN KEY (examination_time) REFERENCES time(time_id) ON DELETE CASCADE,
    FOREIGN KEY (examinator) REFERENCES workers(worker_id) ON DELETE CASCADE
)AUTO_INCREMENT = 1;


-- create patients_discharge table
CREATE TABLE IF NOT EXISTS patients_discharge(
    discharge_id INT NOT NULL AUTO_INCREMENT,
    patient_id INT NOT NULL,
    discharge_date INT NOT NULL,
    discharge_description VARCHAR(500) NOT NULL,
    person_discharging INT NOT NULL,
    discharge_on_demand BOOL NOT NULL,
    PRIMARY KEY(discharge_id, patient_id),
    FOREIGN KEY(patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY(discharge_date) REFERENCES date(date_id) ON DELETE CASCADE,
    FOREIGN KEY(person_discharging) REFERENCES workers(worker_id) ON DELETE CASCADE
)AUTO_INCREMENT = 1;


-- create patients_doctors table
CREATE TABLE IF NOT EXISTS patients_doctors(
    p_d_id INT NOT NULL AUTO_INCREMENT,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    PRIMARY KEY(p_d_id),
    FOREIGN KEY(patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY(doctor_id) REFERENCES workers(worker_id) ON DELETE CASCADE
)AUTO_INCREMENT = 1;


-- create patients_nurses table
CREATE TABLE IF NOT EXISTS patients_nurses(
    p_n_id INT NOT NULL AUTO_INCREMENT,
    patient_id INT NOT NULL,
    nurse_id INT NOT NULL,
    PRIMARY KEY(p_n_id),
    FOREIGN KEY(patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY(nurse_id) REFERENCES workers(worker_id) ON DELETE CASCADE
)AUTO_INCREMENT = 1;


-- create equipment_producent table
CREATE TABLE IF NOT EXISTS equipment_producent(
    producent_id INT NOT NULL AUTO_INCREMENT,
    producent_name VARCHAR(50) NOT NULL,
    phone INT(9),
    email VARCHAR(50) NOT NULL,
    PRIMARY KEY(producent_id)
)AUTO_INCREMENT = 1;


-- create equipment_type table
CREATE TABLE IF NOT EXISTS equipment_type(
    et_id INT NOT NULL AUTO_INCREMENT,
    e_type VARCHAR(100),
    PRIMARY KEY(et_id)
)AUTO_INCREMENT = 1;


-- create equipment table
CREATE TABLE IF NOT EXISTS equipment(
    eq_id INT NOT NULL AUTO_INCREMENT,
    eq_type INT NOT NULL,
    eq_producent INT NOT NULL,
    PRIMARY KEY(eq_id),
    FOREIGN KEY(eq_type) REFERENCES equipment_type(et_id) ON DELETE CASCADE,
    FOREIGN KEY(eq_producent) REFERENCES equipment_producent(producent_id) ON DELETE CASCADE
)AUTO_INCREMENT = 1;


-- create room_type table
CREATE TABLE IF NOT EXISTS room_type(
    type_id INT NOT NULL AUTO_INCREMENT,
    room_type VARCHAR(20) NOT NULL,
    PRIMARY KEY(type_id)
)AUTO_INCREMENT = 1;


-- create rooms table
CREATE TABLE IF NOT EXISTS rooms(
    room_id INT NOT NULL AUTO_INCREMENT,
    room_number INT NOT NULL,
    department_id INT NOT NULL,
    room_type INT NOT NULL,
    PRIMARY KEY(room_id),
    FOREIGN KEY(room_type) REFERENCES room_type(type_id) ON DELETE CASCADE,
    FOREIGN KEY(department_id) REFERENCES department(department_id) ON DELETE CASCADE
)AUTO_INCREMENT = 1;


-- create room_equipment table
CREATE TABLE IF NOT EXISTS room_equipment(
    id INT NOT NULL AUTO_INCREMENT,
    room_id INT NOT NULL,
    eq_id INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(room_id) REFERENCES rooms(room_id) ON DELETE CASCADE,
    FOREIGN KEY(eq_id) REFERENCES equipment(eq_id) ON DELETE CASCADE
)AUTO_INCREMENT = 1;

-- 
-- create status table
CREATE TABLE IF NOT EXISTS status(
    status_id INT NOT NULL AUTO_INCREMENT,
    status VARCHAR(50) NOT NULL,
    PRIMARY KEY(status_id)
)AUTO_INCREMENT = 1;


-- create appointments_schedule table
CREATE TABLE IF NOT EXISTS appointments_schedule(
    app_id INT NOT NULL AUTO_INCREMENT,
    patient_id INT NOT NULL,
    department_id INT NOT NULL,
    app_date_id INT NOT NULL,
    app_hour_id INT NOT NULL, 
    app_status_id INT NOT NULL,
    PRIMARY KEY(app_id),
    FOREIGN KEY(patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY(department_id) REFERENCES department(department_id) ON DELETE CASCADE,
    FOREIGN KEY(app_date_id) REFERENCES date(date_id) ON DELETE CASCADE,
    FOREIGN KEY(app_hour_id) REFERENCES time(time_id) ON DELETE CASCADE,
    FOREIGN KEY(app_status_id) REFERENCES status(status_id) ON DELETE CASCADE
)AUTO_INCREMENT = 1;


-- create examinations_schedule table
CREATE TABLE IF NOT EXISTS examinations_schedule(
    exam_id INT NOT NULL AUTO_INCREMENT,
    patient_id INT NOT NULL,
    room_id INT NOT NULL,
    exam_date_id INT NOT NULL,
    exam_hour_id INT NOT NULL, 
    exam_status_id INT NOT NULL,
    PRIMARY KEY(exam_id),
    FOREIGN KEY(patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY(room_id) REFERENCES rooms(room_id) ON DELETE CASCADE,
    FOREIGN KEY(exam_date_id) REFERENCES date(date_id) ON DELETE CASCADE,
    FOREIGN KEY(exam_hour_id) REFERENCES time(time_id) ON DELETE CASCADE,
    FOREIGN KEY(exam_status_id) REFERENCES status(status_id) ON DELETE CASCADE
)AUTO_INCREMENT = 1;


-- create surgeries_schedule table
CREATE TABLE IF NOT EXISTS surgeries_schedule(
    schedule_id INT NOT NULL AUTO_INCREMENT,
    patient_id INT NOT NULL,
    worker_id INT NOT NULL,
    room_id INT NOT NULL,
    date_id INT NOT NULL,
    time_id INT NOT NULL,
    status_id INT NOT NULL,
    surgery_type_id INT NOT NULL,
    PRIMARY KEY (schedule_id),
    FOREIGN KEY (patient_id) REFERENCES patients (patient_id) ON DELETE CASCADE,
    FOREIGN KEY (worker_id) REFERENCES workers(worker_id) ON DELETE CASCADE,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id) ON DELETE CASCADE,
    FOREIGN KEY (date_id) REFERENCES date(date_id) ON DELETE CASCADE,
    FOREIGN KEY (time_id) REFERENCES time(time_id) ON DELETE CASCADE,
    FOREIGN KEY (status_id) REFERENCES status(status_id) ON DELETE CASCADE,
    FOREIGN KEY (surgery_type_id) REFERENCES surgeries(surgery_id) ON DELETE CASCADE
) AUTO_INCREMENT = 1;


-- create patients_rooms table
CREATE TABLE IF NOT EXISTS patients_rooms(
    id INT NOT NULL AUTO_INCREMENT,
    patient_id INT NOT NULL,
    room_id INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY(room_id) REFERENCES rooms(room_id) ON DELETE CASCADE
) AUTO_INCREMENT = 1;


-- create rooms_to_clean table
CREATE TABLE IF NOT EXISTS rooms_to_clean(
    id INT NOT NULL AUTO_INCREMENT,
    room_id INT NOT NULL,
    need_cleaning BOOL NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(room_id) REFERENCES rooms(room_id) ON DELETE CASCADE
) AUTO_INCREMENT = 1;


-- create equipment_repairs table
CREATE TABLE IF NOT EXISTS equipment_repairs(
    id INT NOT NULL AUTO_INCREMENT,
    equipment_id INT NOT NULL,
    room_id INT NOT NULL,
    need_repair BOOL NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(equipment_id) REFERENCES equipment(eq_id) ON DELETE CASCADE,
    FOREIGN KEY(room_id) REFERENCES rooms(room_id) ON DELETE CASCADE
) AUTO_INCREMENT = 1;




