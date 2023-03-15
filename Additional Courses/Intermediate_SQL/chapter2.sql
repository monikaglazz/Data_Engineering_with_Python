SELECT title
FROM films
WHERE release_year > 2000;

-- Select film_ids and imdb_score with an imdb_score over 7.0
select film_id, imdb_score from reviews where imdb_score > 7.0;

-- Count the Spanish-language films
select count(*) as count_spanish from films where language = 'Spanish'

-- Select the title and release_year for all German-language films released before 2000
select title, release_year from films where language = 'German' and release_year < 2000;

-- Find the title and year of films from the 1990 or 1999
select title, release_year from films where release_year = 1990 or release_year = 1999;

-- Select the title and release_year for films released between 1990 and 2000
select title, release_year from films where release_year between 1990 and 2000;

-- Select the names that start with B
SELECT name FROM people WHERE name LIKE 'B%';

-- Find the title and release_year for all films over two hours in length released in 1990 and 2000
select title, release_year from films where release_year in (1990, 2000) and duration > 120;

-- Count the unique titles
SELECT Count(distinct title) AS nineties_english_films_for_teens
FROM films
-- Filter to release_years to between 1990 and 1999
WHERE release_year between 1990 and 1999
-- Filter to English-language films
	and language = 'English'
-- Narrow it down to G, PG, and PG-13 certifications
	and certification in ('G','PG','PG-13');

-- List all film titles with missing budgets
select title as no_budget_info from films where budget is null;