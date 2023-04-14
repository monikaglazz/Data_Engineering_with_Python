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
    fuction_id INT NOT NULL AUTO_INCREMENT,
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
    contract_start DATE NOT NULL DEFAULT NOW(),
    contract_end DATE,
    salary INT NOT NULL,
    PRIMARY KEY(worker_id),
    FOREIGN KEY(worker_type) REFERENCES workers_type(type_id) ON DELETE CASCADE,
    FOREIGN KEY(worker_department) REFERENCES departments(department_id) ON DELETE CASCADE,
    FOREIGN KEY(address) REFERENCES workers_address(address_id) ON DELETE CASCADE,
    FOREIGN KEY(specialization) REFERENCES specializations(specialization_id) ON DELETE CASCADE
)AUTO_INCREMENT = 1;


CREATE TABLE workers_responsibilities(
    res_id INT NOT NULL AUTO_INCREMENT,
    worker_id INT NOT NULL,
    function_id INT NOT NULL,
    PRIMARY KEY(res_id),
    FOREIGN KEY(worker_id) REFERENCES workers(worker_id) ON DELETE CASCADE,
    FOREIGN KEY(function_id) REFERENCES responsibilities(function_id) ON DELETE CASCADE,
)AUTO_INCREMENT = 1;

-- create patients_address table
CREATE TABLE IF NOT EXISTS patients_address(
    
)AUTO_INCREMENT = 1;


-- create patients table
CREATE TABLE IF NOT EXISTS patients()AUTO_INCREMENT = 1;


-- create medicines table
CREATE TABLE IF NOT EXISTS medicines()AUTO_INCREMENT = 1;


-- create surgeries table
CREATE TABLE IF NOT EXISTS surgeries()AUTO_INCREMENT = 1;


-- create examinations table
CREATE TABLE IF NOT EXISTS examinations()AUTO_INCREMENT = 1;


-- create patient_medicines table
CREATE TABLE IF NOT EXISTS patient_medicines()AUTO_INCREMENT = 1;


-- create patient_surgeries table
CREATE TABLE IF NOT EXISTS patient_surgeries()AUTO_INCREMENT = 1;


-- create patient_examinations table
CREATE TABLE IF NOT EXISTS patient_examinations()AUTO_INCREMENT = 1;


-- create patients_discharge table
CREATE TABLE IF NOT EXISTS patients_discharge()AUTO_INCREMENT = 1;


-- create patients_doctors table
CREATE TABLE IF NOT EXISTS patients_doctors()AUTO_INCREMENT = 1;


-- create patients_nurses table
CREATE TABLE IF NOT EXISTS patients_nurses()AUTO_INCREMENT = 1;


-- create appointment_time table
CREATE TABLE IF NOT EXISTS appointment_time()AUTO_INCREMENT = 1;


-- create appointment_date table
CREATE TABLE IF NOT EXISTS appointment_date()AUTO_INCREMENT = 1;


-- create appointment_status table
CREATE TABLE IF NOT EXISTS appointment_status()AUTO_INCREMENT = 1;


-- create appointments_schedule table
CREATE TABLE IF NOT EXISTS appointments_schedule()AUTO_INCREMENT = 1;


-- create examination_time table
CREATE TABLE IF NOT EXISTS examination_time()AUTO_INCREMENT = 1;


-- create examination_date table
CREATE TABLE IF NOT EXISTS examination_date()AUTO_INCREMENT = 1;


-- create examination_status table
CREATE TABLE IF NOT EXISTS examination_status()AUTO_INCREMENT = 1;


-- create examinations_schedule table
CREATE TABLE IF NOT EXISTS examinations_schedule()AUTO_INCREMENT = 1;


-- create surgery_time table
CREATE TABLE IF NOT EXISTS surgery_time()AUTO_INCREMENT = 1;


-- create surgery_date table
CREATE TABLE IF NOT EXISTS surgery_date()AUTO_INCREMENT = 1;


-- create surgeries_schedule table
CREATE TABLE IF NOT EXISTS surgeries_schedule()AUTO_INCREMENT = 1;


-- create demand_status table
CREATE TABLE IF NOT EXISTS demand_status()AUTO_INCREMENT = 1;


-- create suplies_type table
CREATE TABLE IF NOT EXISTS suplies_type()AUTO_INCREMENT = 1;


-- create suplies table
CREATE TABLE IF NOT EXISTS suplies()AUTO_INCREMENT = 1;


-- create equipment_producent table
CREATE TABLE IF NOT EXISTS equipment_producent()AUTO_INCREMENT = 1;


-- create equipment table
CREATE TABLE IF NOT EXISTS equipment()AUTO_INCREMENT = 1;


-- create room_type table
CREATE TABLE IF NOT EXISTS room_type()AUTO_INCREMENT = 1;


-- create rooms table
CREATE TABLE IF NOT EXISTS rooms()AUTO_INCREMENT = 1;


-- create room_equipment table
CREATE TABLE IF NOT EXISTS room_equipment()AUTO_INCREMENT = 1;

