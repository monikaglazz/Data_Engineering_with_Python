


-- ex 1 "Query information_schema with SELECT"
-- information_schema is a meta-database that holds information about your current database

-- Query the table in information_schema
SELECT table_name 
FROM information_schema.tables
-- Specify the correct table_schema value
WHERE table_schema = 'public';

-- Query the table in information_schema to get columns
SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'university_professors' AND table_schema = 'public';

-- Query the first five rows of our table
SELECT * 
FROM university_professors 
LIMIT 5;

-- ex 2 "CREATE your first few TABLEs"
-- Create a table for the universities entity type
-- Create a table for the professors entity type
CREATE TABLE professors (
 firstname text,
 lastname text
);

CREATE TABLE universities (
    university_shortname text,
    university text,
    university_city text
);



-- ex 3 "ADD a COLUMN with ALTER TABLE"
-- Add the university_shortname column
ALTER TABLE professors
ADD COLUMN university_shortname text;



-- ex 4 "RENAME and DROP COLUMNs in affiliations"
-- Rename the organisation column
ALTER TABLE affiliations
RENAME COLUMN organisation TO organization;

-- Delete the university_shortname column
ALTER TABLE affiliations
DROP COLUMN university_shortname;



-- ex 5 "Migrate data with INSERT INTO SELECT DISTINCT"
-- Insert unique professors into the new table
INSERT INTO professors 
SELECT DISTINCT firstname, lastname, university_shortname 
FROM university_professors;

-- Doublecheck the contents of professors
SELECT * 
FROM professors;

-- Insert unique affiliations into the new table
INSERT INTO affiliations 
SELECT DISTINCT firstname, lastname, function, organization 
FROM university_professors;

-- Doublecheck the contents of affiliations
SELECT * 
FROM affiliations;

-- ex 6 "Delete tables with DROP TABLE"
-- Delete the university_professors table
DROP TABLE university_professors;