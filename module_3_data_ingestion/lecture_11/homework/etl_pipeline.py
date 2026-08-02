# 1. Создан файл etl_pipeline.py

# 2. Импортируем необходимые библиотеки
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# 3. Настраиваем строку подключения к базе данных
DB_USER = "admin"
DB_PASSWORD = "admin123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "postgres"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# 4. Инициализируем объект Engine через create_engine
engine = create_engine(DATABASE_URL)

# 5. Реализуем базовую обработку ошибок подключения (try-except)
try:
    # Пытаемся подключиться к базе данных
    with engine.connect() as conn:
        print("Подключение к базе данных успешно установлено.")

        # Проверяем, что база данных доступна
        conn.execute(text("SELECT 1"))
        print("База данных доступна.")

except SQLAlchemyError as e:
    # Если ошибка — выводим сообщение и завершаем программу
    print(f"Ошибка подключения к базе данных: {e}")
    exit(1)

print("Настройка соединения завершена.")

# --- Этап 2: Загрузка таблиц-справочников ---
print("\nНачинаем загрузку справочников...")

# 1. Загрузка таблицы countries
countries_df = pd.read_csv("countries.csv", sep=';')
countries_df.to_sql("bronze_countries", engine, if_exists="replace", index=False)
print("Таблица 'bronze_countries' загружена")

# 2. Загрузка таблицы cities
cities_df = pd.read_csv("cities.csv", sep=';')
cities_df.to_sql("bronze_cities", engine, if_exists="replace", index=False)
print("Таблица 'bronze_cities' загружена")

# 3. Загрузка таблицы categories
categories_df = pd.read_csv("categories.csv", sep=';')
categories_df.to_sql("bronze_categories", engine, if_exists="replace", index=False)
print("Таблица 'bronze_categories' загружена")

# 4. Загрузка таблицы products
products_df = pd.read_csv("products.csv", sep=';')
products_df.to_sql("bronze_products", engine, if_exists="replace", index=False)
print("Таблица 'bronze_products' загружена")

# 5. Загрузка таблицы shops
shops_df = pd.read_csv("shops.csv", sep=';')
shops_df.to_sql("bronze_shops", engine, if_exists="replace", index=False)
print("Таблица 'bronze_shops' загружена")

# 6. Загрузка таблицы employees
employees_df = pd.read_csv("employees.csv", sep=';')
employees_df.to_sql("bronze_employees", engine, if_exists="replace", index=False)
print("Таблица 'bronze_employees' загружена")

# 7. Загрузка таблицы customers
customers_df = pd.read_csv("customers.csv", sep=';')
customers_df.to_sql("bronze_customers", engine, if_exists="replace", index=False)
print("Таблица 'bronze_customers' загружена")

print("\nВсе таблицы-справочники успешно загружены!")

# --- Этап 3: Загрузка таблицы продаж ---
print("\nНачинаем загрузку таблицы 'sales'...")

# Читаем sales.csv с разделителем ';' и указываем, что файл может быть большим
sales_df = pd.read_csv("sales.csv", sep=';')

# Загружаем данные по частям (батчами) по 5000 строк
chunk_size = 5000  # количество строк за 1 раз

# Разбиваем DataFrame на части и загружаем
for i, chunk in enumerate(range(0, len(sales_df), chunk_size)):
    batch = sales_df.iloc[chunk:chunk + chunk_size]
    batch.to_sql(
        "bronze_sales",
        engine,
        if_exists="replace" if i == 0 else "append",
        index=False
    )
    print(f"Загружено строк: {chunk + len(batch)}")

print("Таблица 'bronze_sales' полностью загружена!")
