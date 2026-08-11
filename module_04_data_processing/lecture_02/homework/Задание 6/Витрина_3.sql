# Витрина 3: mart_customer_behavior

CREATE OR REPLACE VIEW mart.mart_customer_behavior AS
WITH max_date AS (
    SELECT MAX(full_date) AS last_date FROM gold.dim_date
),
customer_metrics AS (
    SELECT 
        f.customer_sk,
        SUM(f.total_price) AS total_spent,
        COUNT(DISTINCT f.sales_id) AS order_count,
        MIN(d.full_date) AS first_purchase,
        MAX(d.full_date) AS last_purchase,
        (SELECT last_date FROM max_date) - MAX(d.full_date) AS days_since_last_purchase
    FROM gold.fact_sales f
    JOIN gold.dim_date d ON f.date_key = d.date_key
    GROUP BY f.customer_sk
)
SELECT 
    CASE 
        WHEN days_since_last_purchase <= 30 THEN 'Active'
        WHEN days_since_last_purchase <= 90 THEN 'At Risk'
        ELSE 'Inactive'
    END AS activity_status,
    CASE 
        WHEN total_spent >= 1000 THEN 'Premium'
        WHEN total_spent >= 500 THEN 'Regular'
        ELSE 'Basic'
    END AS customer_segment,
    COUNT(*) AS customer_count,
    ROUND(AVG(total_spent), 2) AS avg_spent,
    SUM(total_spent) AS total_segment_revenue
FROM customer_metrics
GROUP BY activity_status, customer_segment
ORDER BY activity_status, customer_segment;


SELECT * FROM mart.mart_customer_behavior;


