SELECT 
    e.first_name,
    e.last_name,
    sh.address,
    s.total_price AS max_amount
FROM sales s
JOIN employees e ON s.employee_id = e.employee_id
JOIN shops sh ON e.shop_id = sh.shop_id
WHERE s.total_price = (SELECT MAX(total_price) FROM sales);