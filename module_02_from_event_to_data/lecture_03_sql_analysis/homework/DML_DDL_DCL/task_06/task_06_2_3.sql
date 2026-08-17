BEGIN;

UPDATE products 
SET class = 'A'
WHERE category_id IN (
    SELECT p.category_id
    FROM products p
    JOIN sales s ON p.product_id = s.product_id
    GROUP BY p.category_id
    HAVING SUM(s.total_price) > 5000
);

UPDATE products 
SET modify_timestamp = NOW()
WHERE modify_timestamp IS NULL;

COMMIT;


SELECT product_name, class, modify_timestamp 
FROM products 
WHERE category_id IN (1, 2, 3) 
LIMIT 10;