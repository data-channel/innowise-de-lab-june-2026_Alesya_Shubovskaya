WITH shop_stats AS (
    SELECT 
        co.country_name,
        sh.shop_id,
        sh.address as shop_address,
        COUNT(s.sale_id) AS total_sales_count,
        SUM(s.total_price) AS total_sales_amount
    FROM sales s
    JOIN employees e ON s.employee_id = e.employee_id
    JOIN shops sh ON e.shop_id = sh.shop_id
    JOIN cities c ON sh.city_id = c.city_id
    JOIN countries co ON c.country_id = co.country_id
    GROUP BY co.country_name, sh.shop_id, sh.address
    HAVING COUNT(s.sale_id) >= 2
),
country_totals AS (
    SELECT 
        country_name,
        SUM(total_sales_amount) AS country_total_sales
    FROM shop_stats
    GROUP BY country_name
)
SELECT 
    ss.country_name,
    ss.shop_id,
    ss.shop_address,
    ss.total_sales_count,
    ss.total_sales_amount,
    ct.country_total_sales,
    ROUND(ss.total_sales_amount / ct.country_total_sales * 100, 2) AS country_sales_share,
    RANK() OVER (PARTITION BY ss.country_name ORDER BY ss.total_sales_amount DESC) AS shop_rank,
    SUM(ss.total_sales_amount) OVER (PARTITION BY ss.country_name ORDER BY ss.total_sales_amount DESC) AS country_running_total
FROM shop_stats ss
JOIN country_totals ct ON ss.country_name = ct.country_name
ORDER BY ss.country_name, shop_rank
LIMIT 22;