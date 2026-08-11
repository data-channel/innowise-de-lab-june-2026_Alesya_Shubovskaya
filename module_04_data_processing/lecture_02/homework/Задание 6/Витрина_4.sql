# Витрина 4: mart_employee_performance

CREATE OR REPLACE VIEW mart.mart_employee_performance AS
SELECT 
    e.employee_id,
    e.first_name || ' ' || e.last_name,
    'Магазин №' || s.shop_id AS shop_name,
    COUNT(DISTINCT f.sales_id) AS total_transactions,
    SUM(f.total_price) AS gross_revenue,
    SUM(f.net_price) AS net_revenue,
    ROUND(AVG(f.total_price), 2) AS avg_transaction_value,
    RANK() OVER (ORDER BY SUM(f.net_price) DESC) AS revenue_rank
FROM gold.fact_sales f
JOIN gold.dim_employee e ON f.employee_sk = e.employee_sk
JOIN gold.dim_shop s ON f.shop_sk = s.shop_sk
GROUP BY e.employee_id, e.first_name, e.last_name, s.shop_id
ORDER BY revenue_rank;


SELECT * FROM mart.mart_employee_performance LIMIT 15;
