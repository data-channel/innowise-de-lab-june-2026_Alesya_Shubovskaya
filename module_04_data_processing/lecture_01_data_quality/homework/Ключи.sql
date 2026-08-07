alter table silver.silver_categories add primary key (category_id);
alter table silver.silver_cities add primary key (city_id);
alter table silver.silver_countries add primary key (country_id);
alter table silver.silver_customers add primary key (customer_id);
alter table silver.silver_employees add primary key (employee_id);
alter table silver.silver_products add primary key (product_id);
alter table silver.silver_sales add primary key (sales_id);
alter table silver.silver_shops add primary key (shop_id);


alter table silver.silver_sales add foreign key (employee_id) references silver.silver_employees(employee_id);
alter table silver.silver_sales add foreign key (customer_id) references silver.silver_customers(customer_id);
alter table silver.silver_sales add foreign key (product_id) references silver.silver_products(product_id);
alter table silver.silver_sales add foreign key (shop_id) references silver.silver_shops(shop_id);
alter table silver.silver_sales add foreign key (city_id) references silver.silver_cities(city_id);


SELECT DISTINCT city_id
FROM silver.silver_sales
WHERE city_id NOT IN (SELECT city_id FROM silver.silver_cities);


INSERT INTO silver.silver_cities (city_id, city_name, zipcode, country_id)
SELECT DISTINCT s.city_id, 'Неизвестный город', 0, 1
FROM silver.silver_sales s
WHERE s.city_id NOT IN (SELECT city_id FROM silver.silver_cities);