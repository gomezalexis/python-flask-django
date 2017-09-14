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