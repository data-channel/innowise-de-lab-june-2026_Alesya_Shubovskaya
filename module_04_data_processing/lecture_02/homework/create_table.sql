CREATE TABLE gold.dim_category (
    category_sk SERIAL PRIMARY KEY,
    category_id INT NOT NULL,
    category_name VARCHAR(100) NOT NULL
);


CREATE TABLE gold.dim_employee (
    employee_sk SERIAL PRIMARY KEY,
    employee_id INT NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    shop_id INT
);

CREATE TABLE gold.dim_location (
    location_sk SERIAL PRIMARY KEY,
    city_id INT NOT NULL,
    city_name VARCHAR(100),
    country_name VARCHAR(100)
);


CREATE TABLE gold.dim_date (
    date_key INT PRIMARY KEY,
    full_date DATE NOT NULL,
    day_of_week INT NOT NULL,
    week_num INT NOT NULL,
    month_num INT NOT NULL,
    month_name VARCHAR(20) NOT NULL,
    quarter_num INT NOT NULL,
    year_num INT NOT NULL
);


CREATE TABLE gold.dim_product (
    product_sk SERIAL PRIMARY KEY,
    product_id INT NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    price NUMERIC(10,2) NOT NULL,
    category_id INT
);


CREATE TABLE gold.dim_customer (
    customer_sk SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20),
    city VARCHAR(100),
    valid_from_dt DATE NOT NULL,
    valid_to_dt DATE NOT NULL,
    is_current BOOLEAN NOT NULL
);


CREATE TABLE gold.dim_shop (
    shop_sk SERIAL PRIMARY KEY,
    shop_id INT NOT NULL,
    shop_name VARCHAR(100),
    address VARCHAR(200),
    city_id INT
);


CREATE TABLE gold.fact_sales (
    sale_id BIGINT PRIMARY KEY,
    date_key INT NOT NULL,
    product_sk INT NOT NULL,
    customer_sk INT NOT NULL,
    shop_sk INT NOT NULL,
    employee_sk INT NOT NULL,
    category_sk INT NOT NULL,
    location_sk INT NOT NULL,
    quantity INT NOT NULL,
    discount_amount NUMERIC(10,2),
    total_revenue NUMERIC(10,2) NOT NULL,
    net_revenue NUMERIC(10,2) NOT NULL
);
