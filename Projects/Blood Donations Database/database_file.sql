CREATE DATABASE blood_donations_database;

USE blood_donations_database;

CREATE TABLE country_data (
    country_id INT NOT NULL AUTO_INCREMENT,
    country_name VARCHAR(50),
    PRIMARY KEY(country_id)
);

CREATE TABLE city_data (
    city_id INT NOT NULL AUTO_INCREMENT,
    city_name VARCHAR(50),
    country_id INT,
    PRIMARY KEY(city_id),
    FOREIGN KEY(country_id) REFERENCES country_data(country_id)
);


CREATE TABLE address_data (
    address_id INT NOT NULL AUTO_INCREMENT,
    street_name VARCHAR(50),
    house_number INT,
    apartment_number INT,
    city_id INT,
    PRIMARY KEY(address_id),
    FOREIGN KEY(city_id) REFERENCES city_data(city_id)
);


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
    medical_history VARCHAR(500) NOT NULL,
    honorary_blood_donor_status BOOL,
    PRIMARY KEY(donor_id),
    FOREIGN KEY(address_id) REFERENCES address_data(address_id)
);

CREATE TABLE donations(
    donation_id INT NOT NULL AUTO_INCREMENT,
    donation_date DATETIME NOT NULL,
    blood_amount_l DECIMAL(4,3),
    donor_id INT,
    PRIMARY KEY(donation_id),
    FOREIGN KEY(donor_id) REFERENCES donor_data(donor_id)
);
