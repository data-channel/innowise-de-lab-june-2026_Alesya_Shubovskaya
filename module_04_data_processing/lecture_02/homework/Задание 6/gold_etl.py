import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# Подключение к базе
DB_USER = "admin"
DB_PASSWORD = "admin123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "postgres"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

#================================================
# 1. Загрузка dim_date
query = """
SELECT DISTINCT DATE(sales_timestamp) AS full_date
FROM silver.silver_sales
WHERE sales_timestamp IS NOT NULL
"""
dates_df = pd.read_sql(query, engine)

# Создаём атрибуты для dim_date
def create_date_dimension(df):
    # Преобразуем колонку в дату (если она еще не дата)
    df['full_date'] = pd.to_datetime(df['full_date'], errors='coerce')

    # Удаляем строки, где дата не распозналась (стала NaT)
    df = df.dropna(subset=['full_date'])

    df['date_key'] = df['full_date'].dt.strftime('%Y%m%d').astype(int)
    df['day_of_week'] = df['full_date'].dt.dayofweek + 1  # ПН = 1, ВС = 7
    df['week_num'] = df['full_date'].dt.isocalendar().week
    df['month_num'] = df['full_date'].dt.month
    df['month_name'] = df['full_date'].dt.strftime('%B')
    df['quarter_num'] = df['full_date'].dt.quarter
    df['year_num'] = df['full_date'].dt.year
    return df

dates_df = create_date_dimension(dates_df)

# Загружаем в dim_date (инкрементально)
# Проверяем, какие даты уже есть в таблице
existing_dates = pd.read_sql("SELECT date_key FROM gold.dim_date", engine)
new_dates = dates_df[~dates_df['date_key'].isin(existing_dates['date_key'])]

if not new_dates.empty:
    new_dates[['date_key', 'full_date', 'day_of_week', 'week_num', 'month_num',
               'month_name', 'quarter_num', 'year_num']].to_sql(
        'dim_date', engine, if_exists='append', index=False, schema='gold'
    )
    print(f"Добавлено {len(new_dates)} записей в dim_date")
else:
    print("Новых дат нет")

# =========================================================
# 2. Загрузка dim_product
# Загружаем данные из Silver
query_product = """
SELECT DISTINCT
    product_id,
    product_name,
    price,
    category_id
FROM silver.silver_products
"""
product_df = pd.read_sql(query_product, engine)

# Проверяем, какие product_id уже есть в Gold
existing_ids = pd.read_sql("SELECT product_id FROM gold.dim_product", engine)

# Оставляем только те записи, которых ещё нет
if not existing_ids.empty:
    new_products = product_df[~product_df['product_id'].isin(existing_ids['product_id'])]
else:
    new_products = product_df

# Загружаем только новые записи
if not new_products.empty:
    new_products[['product_id', 'product_name', 'price', 'category_id']].to_sql(
        'dim_product', engine, if_exists='append', index=False, schema='gold'
    )
    print(f"Добавлено {len(new_products)} новых записей в dim_product")
else:
    print("Новых продуктов нет")

# ========================================================
# Загрузка dim_customer
# Загружаем данные из Silver
query_customer = """
SELECT DISTINCT
    customer_id,
    first_name,
    last_name,
    city_id,
    CURRENT_DATE AS valid_from_dt,
    '2099-12-31' AS valid_to_dt,
    TRUE AS is_current
FROM silver.silver_customers
"""
customer_df = pd.read_sql(query_customer, engine)

# Проверяем, какие customer_id уже есть в Gold
existing_ids = pd.read_sql("SELECT customer_id FROM gold.dim_customer", engine)

# Оставляем только новых клиентов
if not existing_ids.empty:
    new_customers = customer_df[~customer_df['customer_id'].isin(existing_ids['customer_id'])]
else:
    new_customers = customer_df

# Загружаем только новых клиентов
if not new_customers.empty:
    new_customers[['customer_id', 'first_name', 'last_name', 'city_id',
                   'valid_from_dt', 'valid_to_dt', 'is_current']].to_sql(
        'dim_customer', engine, if_exists='append', index=False, schema='gold'
    )
    print(f"Добавлено {len(new_customers)} новых записей в dim_customer")
else:
    print("Новых клиентов нет")

# ============================================================
# Загрузка dim_shop
# Загружаем данные из Silver
query_shop = """
SELECT DISTINCT
    shop_id,
    address,
    city_id
FROM silver.silver_shops
"""
shop_df = pd.read_sql(query_shop, engine)

# Проверяем, какие shop_id уже есть в Gold
existing_ids = pd.read_sql("SELECT shop_id FROM gold.dim_shop", engine)

# Оставляем только новые магазины
if not existing_ids.empty:
    new_shops = shop_df[~shop_df['shop_id'].isin(existing_ids['shop_id'])]
else:
    new_shops = shop_df

# Загружаем только новые
if not new_shops.empty:
    new_shops[['shop_id', 'address', 'city_id']].to_sql(
        'dim_shop', engine, if_exists='append', index=False, schema='gold'
    )
    print(f"Добавлено {len(new_shops)} новых записей в dim_shop")
else:
    print("Новых магазинов нет")

# =====================================================
# Загрузка dim_employee
# Загружаем данные из Silver
query_employee = """
SELECT DISTINCT
    employee_id,
    first_name,
    last_name,
    shop_id
FROM silver.silver_employees
"""
employee_df = pd.read_sql(query_employee, engine)

# Проверяем, какие employee_id уже есть в Gold
existing_ids = pd.read_sql("SELECT employee_id FROM gold.dim_employee", engine)

# Оставляем только новых сотрудников
if not existing_ids.empty:
    new_employees = employee_df[~employee_df['employee_id'].isin(existing_ids['employee_id'])]
else:
    new_employees = employee_df

# Загружаем только новых
if not new_employees.empty:
    new_employees[['employee_id', 'first_name', 'last_name', 'shop_id']].to_sql(
        'dim_employee', engine, if_exists='append', index=False, schema='gold'
    )
    print(f"Добавлено {len(new_employees)} новых записей в dim_employee")
else:
    print("Новых сотрудников нет")

# =========================================================
# Загрузка dim_category
# Загружаем данные из Silver
query_category = """
SELECT DISTINCT
    category_id,
    category_name
FROM silver.silver_categories
"""
category_df = pd.read_sql(query_category, engine)

# Проверяем, какие category_id уже есть в Gold
existing_ids = pd.read_sql("SELECT category_id FROM gold.dim_category", engine)

# Оставляем только новые категории
if not existing_ids.empty:
    new_categories = category_df[~category_df['category_id'].isin(existing_ids['category_id'])]
else:
    new_categories = category_df

# Загружаем только новые
if not new_categories.empty:
    new_categories[['category_id', 'category_name']].to_sql(
        'dim_category', engine, if_exists='append', index=False, schema='gold'
    )
    print(f"Добавлено {len(new_categories)} новых записей в dim_category")
else:
    print("Новых категорий нет")

# =========================================================
# Загрузка dim_location
# Загружаем данные из Silver
query_location = """
SELECT DISTINCT
    c.city_id,
    c.city_name,
    co.country_name
FROM silver.silver_cities c
LEFT JOIN silver.silver_countries co ON c.country_id = co.country_id
"""
location_df = pd.read_sql(query_location, engine)

# Проверяем, какие city_id уже есть в Gold
existing_ids = pd.read_sql("SELECT city_id FROM gold.dim_location", engine)

# Оставляем только новые города
if not existing_ids.empty:
    new_locations = location_df[~location_df['city_id'].isin(existing_ids['city_id'])]
else:
    new_locations = location_df

# Загружаем только новые
if not new_locations.empty:
    new_locations[['city_id', 'city_name', 'country_name']].to_sql(
        'dim_location', engine, if_exists='append', index=False, schema='gold'
    )
    print(f"Добавлено {len(new_locations)} новых записей в dim_location")
else:
    print("Новых городов нет")

# ==================================================
# Загрузка fact_sales
# --- Загрузка fact_sales (инкрементальная) ---
print("\n--- Загрузка fact_sales ---")

# 1. Получаем максимальный sales_id из Gold
max_sales_id_query = "SELECT COALESCE(MAX(sales_id), 0) FROM gold.fact_sales"
max_sales_id = pd.read_sql(max_sales_id_query, engine).iloc[0, 0]

# 2. Загружаем новые продажи из Silver
query_sales = f"""
SELECT
    s.sales_id,
    d.date_key,
    p.product_sk,
    c.customer_sk,
    sh.shop_sk,
    e.employee_sk,
    s.quantity,
    s.discount,
    s.total_price,
    s.total_price - s.discount AS net_price
FROM silver.silver_sales s
JOIN gold.dim_date d ON DATE(s.sales_timestamp) = d.full_date
JOIN gold.dim_product p ON s.product_id = p.product_id
JOIN gold.dim_customer c ON s.customer_id = c.customer_id
JOIN gold.dim_shop sh ON s.shop_id = sh.shop_id
JOIN gold.dim_employee e ON s.employee_id = e.employee_id
WHERE s.sales_id > {max_sales_id}           
ORDER BY s.sales_id                         
"""
sales_df = pd.read_sql(query_sales, engine)

# 3. Загружаем только новые продажи
if not sales_df.empty:
    sales_df[['sales_id', 'date_key', 'product_sk', 'customer_sk', 'shop_sk',
              'employee_sk', 'quantity', 'discount', 'total_price', 'net_price']].to_sql(
        'fact_sales', engine, if_exists='append', index=False, schema='gold'
    )
    print(f"Добавлено {len(sales_df)} новых записей в fact_sales")
else:
    print("Новых продаж нет")