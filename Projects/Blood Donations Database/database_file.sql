CREATE DATABASE blood_donations_database;

USE blood_donations_database;

-- Create table country_data
CREATE TABLE country_data (
    country_id INT NOT NULL AUTO_INCREMENT,
    country_name VARCHAR(50),
    PRIMARY KEY(country_id)
);


-- Create table city_data
CREATE TABLE city_data (
    city_id INT NOT NULL AUTO_INCREMENT,
    city_name VARCHAR(50),
    country_id INT,
    PRIMARY KEY(city_id),
    FOREIGN KEY(country_id) REFERENCES country_data(country_id) ON DELETE CASCADE
);


-- Create table address_data
CREATE TABLE address_data (
    address_id INT NOT NULL AUTO_INCREMENT,
    street_name VARCHAR(50),
    house_number INT,
    apartment_number INT,
    city_id INT,
    PRIMARY KEY(address_id),
    FOREIGN KEY(city_id) REFERENCES city_data(city_id) ON DELETE CASCADE
);

-- Create table donor_data
CREATE TABLE donor_data (
    donor_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL,
    gender VARCHAR(20),
    address_id INT,
    phone INT(9) NOT NULL,
    email VARCHAR(50),
    blood_type VARCHAR(5) NOT NULL,
    honorary_blood_donor_status BOOL,
    PRIMARY KEY(donor_id),
    FOREIGN KEY(address_id) REFERENCES address_data(address_id) ON DELETE CASCADE
);

-- Create table donations
CREATE TABLE donations(
    donation_id INT NOT NULL AUTO_INCREMENT,
    donation_date DATETIME NOT NULL,
    blood_amount_l DECIMAL(4,3),
    donor_id INT,
    PRIMARY KEY(donation_id),
    FOREIGN KEY(donor_id) REFERENCES donor_data(donor_id) ON DELETE CASCADE
);

-- Create table medications
CREATE TABLE medications(
    medication_id INT NOT NULL AUTO_INCREMENT,
    medication_name VARCHAR(100) NOT NULL UNIQUE,
    description VARCHAR(200) NOT NULL,
    purpose VARCHAR(50) NOT NULL,
    PRIMARY KEY (medication_id)
);

-- Create table surgeries
CREATE TABLE surgeries(
    surgery_id INT NOT NULL AUTO_INCREMENT,
    surgery_name VARCHAR(50) UNIQUE,
    PRIMARY KEY(surgery_id)
);

  
-- Create table patients_medications
CREATE TABLE patients_medications(
    donor_id INT NOT NULL,
    medication_id INT NOT NULL,
    PRIMARY KEY (donor_id, medication_id),
    FOREIGN KEY (donor_id) REFERENCES donor_data(donor_id) ON DELETE CASCADE,
    FOREIGN KEY (medication_id) REFERENCES medications(medication_id) ON DELETE CASCADE
);

-- Create table patients_surgeries
CREATE TABLE patients_surgeries(
    donor_id INT NOT NULL,
    surgery_id INT NOT NULL,
    surgery_date DATE,
    PRIMARY KEY (donor_id, surgery_id),
    FOREIGN KEY (donor_id) REFERENCES donor_data(donor_id) ON DELETE CASCADE,
    FOREIGN KEY (surgery_id) REFERENCES surgeries(surgery_id) ON DELETE CASCADE
);