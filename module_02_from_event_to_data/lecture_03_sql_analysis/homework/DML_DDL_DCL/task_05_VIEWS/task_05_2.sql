CREATE OR REPLACE VIEW full_stat_shops AS
SELECT 
    sh.shop_id,
    sh.shop_address,
    co.country_name,
    COUNT(s.sale_id) AS total_sales_count,
    SUM(s.total_price) AS total_sales_amount
FROM shops sh
JOIN employees e ON sh.shop_id = e.shop_id
JOIN sales s ON e.employee_id = s.employee_id
JOIN cities c ON sh.city_id = c.city_id
JOIN countries co ON c.country_id = co.country_id
GROUP BY sh.shop_id, sh.shop_address, co.country_name;

select * from full_stat_shops;


