# Витрина 5: mart_product_seasonality

DROP VIEW IF EXISTS mart.mart_product_seasonality;

CREATE OR REPLACE VIEW mart.mart_product_seasonality AS
SELECT 
    cat.category_name AS category,
    d.year_num,
    d.month_name,
    SUM(f.quantity) AS total_quantity,
    SUM(f.total_price) AS total_revenue,
    COUNT(DISTINCT f.sales_id) AS order_count
FROM gold.fact_sales f
JOIN gold.dim_product p ON f.product_sk = p.product_sk
JOIN gold.dim_category cat ON p.category_id = cat.category_id
JOIN gold.dim_date d ON f.date_key = d.date_key
GROUP BY cat.category_name, d.year_num, d.month_num, d.month_name
ORDER BY cat.category_name, d.year_num DESC, d.month_num DESC;


SELECT * FROM mart.mart_product_seasonality LIMIT 20;





