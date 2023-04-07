USE shop_database;

-- Insert data into country_data table
INSERT INTO country_data (country_name) VALUES
    ('United States'),
    ('United Kingdom'),
    ('France'),
    ('Germany'),
    ('Spain'),
    ('Italy'),
    ('Japan'),
    ('China'),
    ('India'),
    ('Brazil'),
    ('Mexico'),
    ('Russia'),
    ('Australia'),
    ('Canada'),
    ('South Africa'),
    ('Nigeria'),
    ('Egypt'),
    ('Kenya'),
    ('Ghana'),
    ('Ethiopia');


-- Insert data into city_data table
INSERT INTO city_data (city_name, country_id) VALUES
    ('New York', 1),
    ('Los Angeles', 1),
    ('London', 2),
    ('Paris', 3),
    ('Berlin', 4),
    ('Madrid', 5),
    ('Rome', 6),
    ('Tokyo', 7),
    ('Shanghai', 8),
    ('Mumbai', 9),
    ('Sao Paulo', 10),
    ('Mexico City', 11),
    ('Moscow', 12),
    ('Sydney', 13),
    ('Toronto', 14),
    ('Cape Town', 15),
    ('Lagos', 16),
    ('Cairo', 17),
    ('Nairobi', 18),
    ('Accra', 19);
    
    
-- Insert data into address_data table
INSERT INTO address_data (street_name, house_number, apartment_number, city_id) VALUES
    ('123 Main St', 1, 101, 1),
    ('456 Oak Ave', 2, NULL, 2),
    ('789 Elm St', 3, 203, 3),
    ('10 Rue de la Paix', 4, NULL, 4),
    ('5 Friedrichstrasse', 5, 3, 5),
    ('20 Calle de Alcala', 6, 105, 6),
    ('15 Via Veneto', 7, NULL, 7),
    ('1-1-1 Yurakucho', 8, 301, 8),
    ('123 Nanjing Rd', 9, 202, 9),
    ('1001 Nariman Point', 10, NULL, 10),
    ('100 Avenida Paulista', 11, 501, 11),
    ('500 Paseo de la Reforma', 12, NULL, 12),
    ('15 Tverskaya St', 13, 702, 13),
    ('100 George St', 14, 201, 14),
    ('123 Long St', 15, 301, 15),
    ('20 Allen Ave', 16, NULL, 16),
    ('30 Tahrir Square', 17, 102, 17),
    ('5 Harambee Ave', 18, NULL, 18),
    ('10 Kojo Thompson Rd', 19, 202, 19);
    
    
-- Insert data into the customers table
INSERT INTO customers (customer_name, customer_surname, customer_email, customer_address)
VALUES
  ('John', 'Doe', 'johndoe@example.com', 1),
  ('Jane', 'Doe', 'janedoe@example.com', 2),
  ('Bob', 'Smith', 'bobsmith@example.com', 3),
  ('Alice', 'Johnson', 'alicejohnson@example.com', 4),
  ('Tom', 'Jones', 'tomjones@example.com', 5),
  ('Mary', 'Williams', 'marywilliams@example.com', 6),
  ('David', 'Brown', 'davidbrown@example.com', 7),
  ('Linda', 'Garcia', 'lindagarcia@example.com', 8),
  ('Michael', 'Miller', 'michaelmiller@example.com', 9),
  ('Karen', 'Davis', 'karendavis@example.com', 10),
  ('Steven', 'Hernandez', 'stevenhernandez@example.com', 11),
  ('Lisa', 'Gonzalez', 'lisagonzalez@example.com', 12),
  ('Kevin', 'Wilson', 'kevinwilson@example.com', 13),
  ('Megan', 'Anderson', 'megananderson@example.com', 14),
  ('Richard', 'Thomas', 'richardthomas@example.com', 15),
  ('Patricia', 'Jackson', 'patriciajackson@example.com', 16),
  ('Joseph', 'White', 'josephwhite@example.com', 17),
  ('Jennifer', 'Martin', 'jennifermartin@example.com', 18),
  ('George', 'Lee', 'georgelee@example.com', 19);

-- Insert data into the customer_cards table
INSERT INTO customer_cards (card_number, customer_id)
VALUES
    (1234567890123456, 41),
  (2345678901234567, 42),
  (3456789012345678, 43),
  (4567890123456789, 44),
  (5678901234567890, 45),
  (6789012345678901, 46),
  (7890123456789012, 47),
  (8901234567890123, 48),
  (9012345678901234, 49);

    
-- Insert data into payment_options table
INSERT INTO payment_options(payment_name, description) VALUES 
    ('Credit Card', 'Pay with your credit card online.'),
    ('PayPal', 'Pay with PayPal.'),
    ('Bank Transfer', 'Transfer money directly from your bank account.'),
    ('Cash on Delivery', 'Pay with cash when your order is delivered.'),
    ('Bitcoin', 'Pay with Bitcoin cryptocurrency.');


-- Insert data into shipping_options table
INSERT INTO shipping_options(shipping_name) VALUES 
    ('Standard Shipping'),
    ('Express Shipping'),
    ('Overnight Shipping'),
    ('Free Shipping'),
    ('Local Pickup');
    

-- Insert data into orders table
INSERT INTO orders (customer_id, order_date, payment_option, shipping_option)
VALUES (41, '2022-01-01', 1, 1),
       (42, '2022-02-02', 2, 2),
       (43, '2022-03-03', 3, 3),
       (44, '2022-04-04', 1, 2),
       (45, '2022-05-05', 2, 3),
       (46, '2022-06-06', 3, 1),
       (47, '2022-07-07', 1, 2),
       (48, '2022-08-08', 2, 3),
       (49, '2022-09-09', 3, 1),
       (50, '2022-10-10', 1, 2),
       (51, '2022-11-11', 2, 3),
       (52, '2022-12-12', 3, 1),
       (53, '2023-01-01', 1, 2),
       (54, '2023-02-02', 2, 3),
       (55, '2023-03-03', 3, 1);

-- Insert data into categories table
INSERT INTO categories (category_name)
VALUES ('Men\'s Clothing'), 
    ('Women\'s Clothing'), 
    ('Kids\' Clothing'), 
    ('Accessories'), 
    ('Shoes'), 
    ('Sportswear'), 
    ('Formal Wear'), 
    ('Swimwear'), 
    ('Underwear'), 
    ('Outerwear'), 
    ('Sleepwear'), 
    ('Activewear'), 
    ('Maternity Clothing'), 
    ('Costumes'), 
    ('Vintage Clothing');
    

-- Insert data into producents table
INSERT INTO producents (producent_name)
VALUES
    ('Nike'),
    ('Adidas'),
    ('Puma'),
    ('New Balance'),
    ('Asics'),
    ('Reebok'),
    ('Under Armour'),
    ('Vans'),
    ('Converse'),
    ('Fila');


-- Insert data into products table
INSERT INTO products (product_name, product_description, producent_id, product_category, product_price)
VALUES
    ('Air Max 90', 'A classic running shoe with a unique design', 1, 1, 119.99),
    ('Superstar', 'A retro sneaker with a shell toe', 2, 1, 89.99),
    ('Suede Classic', 'A classic Puma sneaker with a suede upper', 3, 1, 69.99),
    ('990v5', 'A popular running shoe with a comfortable design', 4, 1, 174.99),
    ('Gel-Kayano 27', 'A reliable running shoe with excellent cushioning', 5, 1, 159.99),
    ('Classic Leather', 'A retro Reebok sneaker with a leather upper', 6, 1, 74.99),
    ('Charged Assert 8', 'A comfortable Under Armour running shoe', 7, 1, 79.99),
    ('Old Skool', 'A classic Vans sneaker with a checkerboard pattern', 8, 1, 64.99),
    ('Chuck Taylor All Star', 'A timeless Converse sneaker', 9, 1, 54.99),
    ('Disruptor II', 'A chunky Fila sneaker with a retro look', 10, 1, 79.99),
    ('Men\'s Leather Jacket', 'Black leather jacket for men', 6, 3, 299.99),
    ('Women\'s Fleece Jacket', 'Soft and warm fleece jacket for women', 9, 3, 79.99),
    ('Men\'s Dress Shirt', 'Classic white dress shirt for men', 4, 4, 49.99),
    ('Women\'s Cocktail Dress', 'Elegant black cocktail dress for women', 8, 4, 159.99),
    ('Men\'s Jeans', 'Dark wash denim jeans for men', 3, 2, 69.99),
    ('Women\'s Skinny Jeans', 'High-waisted skinny jeans for women', 7, 2, 89.99),
    ('Men\'s Athletic Shorts', 'Lightweight and breathable athletic shorts for men', 5, 1, 29.99),
    ('Women\'s Running Shoes', 'Lightweight and supportive running shoes for women', 1, 5, 99.99),
    ('Men\'s Hiking Boots', 'Durable and waterproof hiking boots for men', 2, 5, 199.99),
    ('Women\'s Sandals', 'Stylish and comfortable sandals for women', 10, 5, 49.99);
    
    
-- Example data for order_items table
INSERT INTO order_items (order_id, product_id, quantity)
VALUES
    (31, 1, 2),
    (31, 2, 1),
    (31, 3, 3),
    (32, 2, 2),
    (32, 4, 1),
    (33, 1, 1),
    (33, 3, 2),
    (33, 5, 3),
    (34, 2, 3),
    (34, 4, 2),
    (35, 1, 2),
    (35, 5, 1),
    (36, 3, 1),
    (36, 4, 1),
    (36, 5, 2),
    (37, 2, 2),
    (37, 3, 1),
    (37, 4, 3),
    (38, 1, 3),
    (38, 3, 1);

-- Example data for product_amount table
INSERT INTO products_amount (product_id, amount)
VALUES
    (1, 10),
    (2, 5),
    (3, 15),
    (4, 8),
    (5, 20),
    (6, 12),
    (7, 6),
    (8, 18),
    (9, 3),
    (10, 7),
    (11, 9),
    (12, 14),
    (13, 6),
    (14, 4),
    (15, 11),
    (16, 17),
    (17, 22),
    (18, 13),
    (19, 9),
    (20, 6);
    
    
    
    