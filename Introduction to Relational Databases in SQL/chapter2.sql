-- ex 1 "Conforming with data types"
-- Let's add a record to the table
INSERT INTO transactions (transaction_date, amount, fee) 
VALUES (CAST('2018-09-24' AS date), 5454, '30');



-- ex 2 "Type CASTs"
-- Calculate the net amount as amount + fee
SELECT transaction_date, amount + CAST(fee AS integer) AS net_amount 
FROM transactions;



-- ex 3 "Change types with ALTER COLUMN"
-- Select the university_shortname column
SELECT DISTINCT(university_shortname) 
FROM professors;

-- Specify the correct fixed-length character type
ALTER TABLE professors
ALTER COLUMN university_shortname
TYPE char(3);

-- Change the type of firstname
ALTER TABLE professors
ALTER COLUMN firstname
TYPE varchar(64);



-- ex 4 "Convert types USING a function"
-- Convert the values in firstname to a max. of 16 characters
ALTER TABLE professors 
ALTER COLUMN firstname
TYPE varchar(16)
USING SUBSTRING(firstname FROM 1 FOR 16) 



-- ex 5 "Disallow NULL values with SET NOT NULL"
-- Disallow NULL values in firstname
ALTER TABLE professors 
ALTER COLUMN firstname SET NOT NULL;

-- Disallow NULL values in lastname
ALTER TABLE professors
ALTER COLUMN lastname SET NOT NULL;



-- ex 6 "Make your columns UNIQUE with ADD CONSTRAINT"
-- Make universities.university_shortname unique
ALTER TABLE universities
ADD CONSTRAINT university_shortname_unq UNIQUE(university_shortname);

-- Make organizations.organization unique
ALTER TABLE organizations 
ADD CONSTRAINT organization_unq UNIQUE(organization);