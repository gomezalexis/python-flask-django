#1
SELECT customer.first_name, customer.last_name, customer.email, address.city_id, address.address
FROM customer 
JOIN address ON address.address_id = customer.address_id 
WHERE address.city_id = 312;

#2 
SELECT film.title, film.description, film.release_year, film.rental_rate, film.special_features, category.name
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON category.category_id = film_category.category_id
WHERE category.name = 'comedy';

#3
SELECT actor.actor_id, CONCAT(actor.first_name, ' ', actor.last_name) AS full_name, film.title, film.description, film.release_year
FROM film
JOIN film_actor ON film_actor.film_id = film.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE actor.actor_id = 5;

#4
SELECT customer.first_name, customer.last_name, customer.email, address.address#, customer.store_id, address.city_id
FROM customer
JOIN address ON address.address_id = customer.address_id
WHERE customer.store_id = 1 AND (address.city_id = 1 OR address.city_id = 42 OR address.city_id = 312 OR address.city_id = 459);

#5 
SELECT film.title, film.description, film.release_year, film.rating, film.special_features #actor.actor_id
FROM film
JOIN film_actor ON film_actor.film_id = film.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.rating = 'g' AND film.special_features LIKE '%behind the scenes%' AND actor.actor_id=15;

#6
SELECT film.film_id, film.title, actor.actor_id, concat(actor.first_name, ' ', actor.last_name) AS full_name
FROM film
JOIN film_actor ON film_actor.film_id = film.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.film_id=369;

#7
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name 
FROM film
JOIN film_category ON film_category.film_id = film.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name='drama' AND rental_rate = 2.99;

#8
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name, concat(actor.first_name, ' ', actor.last_name) AS actor_name
FROM category
JOIN film_category ON category.category_id = film_category.category_id
JOIN film ON film_category.film_id = film.film_id
JOIN film_actor ON film_actor.film_id = film.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE first_name='sandra' AND last_name='kilmer' AND category.name='action';

