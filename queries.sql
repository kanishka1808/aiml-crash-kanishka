SELECT *
FROM customers;

SELECT *
FROM products;

SELECT *
FROM orders;

SELECT *
FROM orders
WHERE quantity > 1;

SELECT *
FROM products
WHERE category = 'Electronics';

SELECT *
FROM products
ORDER BY price DESC;

SELECT COUNT(*) AS total_orders
FROM orders;

SELECT
SUM(quantity * price) AS total_revenue
FROM orders o
JOIN products p
ON o.product_id = p.product_id;

SELECT AVG(price)
FROM products;

SELECT
category,
SUM(quantity * price) AS revenue
FROM orders o
JOIN products p
ON o.product_id = p.product_id
GROUP BY category;

SELECT
region,
SUM(quantity * price) AS revenue
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
JOIN products p
ON o.product_id = p.product_id
GROUP BY region;

SELECT *
FROM products
WHERE price = (
    SELECT MAX(price)
    FROM products
);

SELECT
c.name,
o.order_id
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id;

SELECT
c.name,
SUM(quantity * price) AS revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN products p
ON o.product_id = p.product_id
GROUP BY c.name;

SELECT
c.name,
SUM(quantity * price) AS revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN products p
ON o.product_id = p.product_id
GROUP BY c.name
HAVING revenue >
(
    SELECT
    AVG(quantity * price)
    FROM orders o
    JOIN products p
    ON o.product_id = p.product_id
);