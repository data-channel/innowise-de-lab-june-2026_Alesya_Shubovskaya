WITH monthly_sales AS (
    SELECT 
        DATE_TRUNC('month', TO_TIMESTAMP(s.sales_timestamp, 'DD.MM.YYYY HH24:MI')) AS sale_month,
        SUM(s.total_price) AS monthly_revenue
    FROM sales s
    JOIN employees e ON s.employee_id = e.employee_id
    JOIN shops sh ON e.shop_id = sh.shop_id
    JOIN cities c ON sh.city_id = c.city_id
    JOIN countries co ON c.country_id = co.country_id
    WHERE co.country_name = 'Germany'
    GROUP BY DATE_TRUNC('month', TO_TIMESTAMP(s.sales_timestamp, 'DD.MM.YYYY HH24:MI'))
)
SELECT 
    sale_month,
    monthly_revenue,
    LAG(monthly_revenue, 1) OVER (ORDER BY sale_month) AS previous_month_revenue,
    monthly_revenue - LAG(monthly_revenue, 1) OVER (ORDER BY sale_month) AS revenue_iff_vs_previous
FROM monthly_sales
ORDER BY sale_month
LIMIT 24;


