#1
SELECT countries.name, languages.language, languages.percentage
FROM languages
JOIN countries ON languages.country_id = countries.id
WHERE language = 'Slovene' ORDER BY percentage DESC;

#2
SELECT countries.name, COUNT(cities.name) AS total_cities
FROM countries 
JOIN cities ON cities.country_id = countries.id
GROUP BY countries.name
ORDER BY COUNT(cities.name) DESC;

#3
SELECT countries.name, cities.name, cities.population
FROM countries 
JOIN cities ON cities.country_id = countries.id
WHERE countries.name = 'Mexico' AND cities.population > 500000
ORDER BY cities.population DESC;

#4
SELECT countries.name, languages.language, languages.percentage
FROM countries JOIN languages 
ON languages.country_id = countries.id
WHERE percentage > 89.0
ORDER BY percentage DESC;

#5
SELECT name, surface_area, population FROM countries
WHERE surface_area < 501.0 AND population > 100000;

#6
SELECT name, government_form, life_expectancy, capital
FROM countries WHERE government_form = 'Constitutional Monarchy'
AND capital > 200 AND life_expectancy > 75.0;

#7
SELECT countries.name, cities.name, cities.district, cities.population
FROM countries JOIN cities
ON cities.country_id = countries.id
WHERE district = 'Buenos Aires' AND cities.population > 500000;

#8
SELECT region, COUNT(name) AS total_countries FROM countries
GROUP BY region ORDER BY COUNT(name) DESC;

#9 Cities in my country
SELECT cities.name, cities.population
FROM countries 
JOIN cities ON cities.country_id = countries.id
WHERE countries.name = 'Puerto Rico';

