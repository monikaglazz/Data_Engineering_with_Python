CREATE DATABASE shop_database;

USE shop_database;


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

-- Create table adddress_data
CREATE TABLE address_data (
    address_id INT NOT NULL AUTO_INCREMENT,
    street_name VARCHAR(50),
    house_number INT,
    apartment_number INT,
    city_id INT,
    PRIMARY KEY(address_id),
    FOREIGN KEY(city_id) REFERENCES city_data(city_id) ON DELETE CASCADE
);

CREATE TABLE customers(
    customer_id INT NOT NULL AUTO_INCREMENT,
    customer_name VARCHAR(50) NOT NULL,
    customer_surname VARCHAR(50) NOT NULL,
    customer_email VARCHAR(50) NOT NULL,
    customer_address INT NOT NULL,
    PRIMARY KEY(customer_id),
    FOREIGN KEY(customer_address) REFERENCES address_data(address_id) ON DELETE CASCADE
);


-- Create table customer_cards
CREATE TABLE customer_cards(
    card_number BIGINT(16) NOT NULL,
    customer_id INT NOT NULL,
    PRIMARY KEY(card_number),
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);


-- Create table payment_options
CREATE TABLE payment_options (
    payment_id INT NOT NULL AUTO_INCREMENT,
    payment_name VARCHAR(50) NOT NULL,
    description VARCHAR(255),
    PRIMARY KEY (payment_id)
);


-- Create table shipping_options
CREATE TABLE shipping_options (
    shipping_id INT NOT NULL AUTO_INCREMENT,
    shipping_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (shipping_id)
);


-- Create table orders
CREATE TABLE orders(
    order_id INT NOT NULL AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    payment_option INT NOT NULL,
    shipping_option INT NOT NULL,
    PRIMARY KEY (order_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (payment_option) REFERENCES payment_options(payment_id) ON DELETE CASCADE,
    FOREIGN KEY (shipping_option) REFERENCES shipping_options(shipping_id) ON DELETE CASCADE
);


-- Create table categories
CREATE TABLE categories(
    category_id INT NOT NULL AUTO_INCREMENT,
    category_name VARCHAR(50) NOT NULL UNIQUE,
    PRIMARY KEY (category_id)
);


-- Create table producents
CREATE TABLE producents (
    producent_id INT NOT NULL AUTO_INCREMENT,
    producent_name VARCHAR(50) NOT NULL UNIQUE,
    PRIMARY KEY (producent_id)
);


-- Create table products
CREATE TABLE products(
    product_id INT NOT NULL AUTO_INCREMENT,
    product_name VARCHAR(50) NOT NULL,
    product_description VARCHAR(200),
    producent_id INT NOT NULL,
    product_category INT NOT NULL,
    product_price DECIMAL(10,2),
    PRIMARY KEY (product_id),
    FOREIGN KEY (product_category) REFERENCES categories(category_id) ON DELETE CASCADE,
    FOREIGN KEY (producent_id) REFERENCES producents(producent_id) ON DELETE CASCADE
);


-- Create table order_items
CREATE TABLE order_items (
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);


-- Create table products_amount
CREATE TABLE products_amount(
    product_id INT NOT NULL,
    amount INT NOT NULL,
    PRIMARY KEY (product_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);