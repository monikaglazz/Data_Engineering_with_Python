-- Select name from people and sort alphabetically
select name from people order by name;

-- Select the release year, duration, and title sorted by release year and duration
select release_year, duration, title from films order by release_year, duration;

-- Find the release_year and film_count of each year
select release_year, count(*) as film_count from films group by release_year;

-- Find the release_year, country, and max_budget, then group and order by release_year and country
select release_year, country, MAX(budget) as max_budget from films group by release_year, country order by release_year, country;


-- Select the country and distinct count of certification as certification_count
select country, count(distinct certification) as certification_count from films
-- Group by country
group by country
-- Filter results to countries with more than 10 different certifications
having count(distinct certification) > 10;


-- Select the country and average_budget from films
select country, round(avg(budget), 2) as average_budget from films
-- Group by country
group by country
-- Filter to countries with an average_budget of more than one billion
having round(avg(budget), 2) > 1000000000
-- Order by descending order of the aggregated budget
order by average_budget desc;

-- Select the budget for films released after 1990 grouped by year
select release_year from films group by release_year having release_year > 1990;