-- Query the sum of film durations
select sum(duration) as total_duration from films;

-- Calculate the sum of gross from the year 2000 or later
select sum(gross) as total_gross from films where release_year >= 2000;

-- Round the average number of facebook_likes to one decimal place
select round(avg(facebook_likes), 1) as avg_facebook_likes from reviews;

-- Calculate the average budget rounded to the thousands
select round(avg(budget), -3) as avg_budget_thousands from films;

-- Calculate the title and duration_hours from films
SELECT title, (duration / 60.0) as duration_hours
FROM films;

-- Round duration_hours to two decimal places
SELECT title, round((duration / 60.0), 2) AS duration_hours
FROM films;