

CREATE OR REPLACE VIEW mart.mart_shop_daily AS
SELECT 
    s.shop_id,
    'Магазин №' || s.shop_id AS shop_name,
    s.address,
    l.city_name AS city,
    l.country_name AS country,
    d.full_date,
    SUM(f.total_price) AS daily_revenue,
    SUM(f.quantity) AS items_sold,
    COUNT(DISTINCT f.sales_id) AS orders_count,
    COUNT(DISTINCT f.customer_sk) AS unique_customers,
    ROUND(AVG(f.total_price), 2) AS avg_check
FROM gold.fact_sales f
JOIN gold.dim_shop s ON f.shop_sk = s.shop_sk
JOIN gold.dim_location l ON s.city_id = l.city_id
JOIN gold.dim_date d ON f.date_key = d.date_key
GROUP BY s.shop_id, s.address, l.city_name, l.country_name, d.full_date
ORDER BY d.full_date DESC;

SELECT * FROM mart.mart_shop_daily LIMIT 15;