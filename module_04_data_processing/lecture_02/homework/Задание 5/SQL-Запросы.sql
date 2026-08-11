# Запрос №1: Выручка по месяцам и магазинам

SELECT 
    d.year_num as Year,                   -- Год (из таблицы дат)
    d.month_num as Month,                 -- Номер месяца (из таблицы дат)
    'Магазин №' || s.shop_id as Shop,     -- Номер магазина (из таблицы магазинов)
    SUM(f.total_price) AS total_revenue   -- Суммируем выручку
FROM gold.fact_sales f
JOIN gold.dim_date d ON f.date_key = d.date_key
JOIN gold.dim_shop s ON f.shop_sk = s.shop_sk
GROUP BY d.year_num, d.month_num, s.shop_id
ORDER BY d.year_num DESC, d.month_num DESC, total_revenue DESC
LIMIT 10;


# Запрос №2: Топ-10 клиентов 

SELECT
    c.customer_id,
    c.first_name || ' ' || c.last_name AS full_name,
    l.city_name AS City,
    COUNT(DISTINCT f.sales_id) AS orders_count,   -- Сколько раз покупал
    SUM(f.quantity) AS total_items,               -- Сколько всего товаров купил
    SUM(f.total_price) AS total_spent             -- Сколько всего потратил
FROM gold.fact_sales f
JOIN gold.dim_customer c ON f.customer_sk = c.customer_sk
JOIN gold.dim_location l ON c.city_id = l.city_id
GROUP BY c.customer_id, c.first_name, c.last_name, l.city_name
ORDER BY total_spent DESC
LIMIT 10;


# Запрос №3: Анализ продаж по сотрудникам

SELECT
e.employee_id,
e.first_name || ' ' || e.last_name AS full_name,
'Магазин №' || s.shop_id as Shop,
COUNT(DISTINCT f.sales_id) AS transactions,        -- Сколько чеков пробил
SUM(f.total_price) AS total_revenue,               -- Сколько денег принёс
ROUND(AVG(f.total_price), 2) AS avg_check          -- Средний чек
FROM gold.fact_sales f
JOIN gold.dim_employee e ON f.employee_sk = e.employee_sk
JOIN gold.dim_shop s ON f.shop_sk = s.shop_sk 
GROUP BY e.employee_id, e.first_name, e.last_name, s.shop_id
ORDER BY total_revenue DESC
LIMIT 15;


# Запрос №4: Самые продаваемые товары   

SELECT 
    p.product_name,
    c.category_name,
    SUM(f.quantity) AS total_sold,      -- Сколько штук продано
    SUM(f.total_price) AS revenue,      -- Сколько денег принёс
    COUNT(DISTINCT f.sales_id) AS transactions    -- В скольких чеках
FROM gold.fact_sales f
JOIN gold.dim_product p ON f.product_sk = p.product_sk 
JOIN gold.dim_category c ON p.category_id = c.category_id 
GROUP BY p.product_name, c.category_name
ORDER BY total_sold DESC
LIMIT 25;




