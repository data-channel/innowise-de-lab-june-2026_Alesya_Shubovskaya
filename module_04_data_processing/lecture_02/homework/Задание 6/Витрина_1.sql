# Витрина 1: mart_daily_anomaly

-- Шаг 1: Создаем схему, если ее нет
CREATE SCHEMA IF NOT EXISTS mart;

-- Шаг 2: Создаем представление
CREATE OR REPLACE VIEW mart.mart_daily_anomaly AS
WITH daily_revenue AS (
    -- Считаем выручку по каждому магазину за каждый день
    SELECT 
        d.full_date,
        f.shop_sk,
        SUM(f.total_price) AS revenue,
        COUNT(DISTINCT f.sales_id) AS transaction_count
    FROM gold.fact_sales f
    JOIN gold.dim_date d ON f.date_key = d.date_key
    GROUP BY d.full_date, f.shop_sk
),
expected_revenue AS (
    -- Считаем ожидаемую выручку (среднее за предыдущие 30 дней)
    SELECT 
        full_date,
        shop_sk,
        revenue,
        AVG(revenue) OVER (
            PARTITION BY shop_sk 
            ORDER BY full_date 
            ROWS BETWEEN 30 PRECEDING AND 1 PRECEDING
        ) AS expected_revenue
    FROM daily_revenue
)
-- Финальный результат
SELECT 
    full_date,
    shop_sk,
    revenue,
    ROUND(COALESCE(expected_revenue, revenue), 2) AS expected_revenue,
    ROUND(
        (revenue - COALESCE(expected_revenue, revenue)) / NULLIF(COALESCE(expected_revenue, revenue), 0) * 100, 
        2
    ) AS uplift_percent,
    CASE 
        WHEN revenue > COALESCE(expected_revenue, revenue) * 1.2 THEN 'High'
        WHEN revenue < COALESCE(expected_revenue, revenue) * 0.8 THEN 'Low'
        ELSE 'Normal'
    END AS anomaly_status
FROM expected_revenue
ORDER BY full_date DESC;


SELECT * FROM mart.mart_daily_anomaly LIMIT 20;

