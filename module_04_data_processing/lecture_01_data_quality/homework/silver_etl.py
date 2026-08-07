import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# --- 1. Подключение к базе данных ---
DB_USER = "admin"
DB_PASSWORD = "admin123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "postgres"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

print("Подключение к базе данных установлено.")

# --- 2. Функция валидации дат (для employees) ---
def validate_and_fix_date(date_str):
    """
    Проверяет и исправляет дату.
    Если дата некорректна — заменяет на 1900-01-01.
    """
    if pd.isna(date_str) or date_str == "":
        return "1900-01-01"

    formats = ["%Y-%m-%d", "%d.%m.%Y", "%m/%d/%Y", "%Y/%m/%d"]

    for fmt in formats:
        try:
            dt = datetime.strptime(str(date_str).strip(), fmt)
            if 1900 <= dt.year <= 2100 and 1 <= dt.month <= 12 and 1 <= dt.day <= 31:
                return dt.strftime("%Y-%m-%d")
        except ValueError:
            continue

    return "1900-01-01"

# --- 3. Обработка таблицы employees ---
print("\nОбработка employees...")

employees_df = pd.read_sql_table("bronze_employees", engine)
employees_df['birth_date'] = employees_df['birth_date'].apply(validate_and_fix_date)
employees_df.to_sql("silver_employees", engine, if_exists="append", index=False)

print("Данные employees загружены в silver_employees")

# --- 4. Обработка таблицы sales (восстановление времени) ---
print("\nОбработка sales...")

sales_df = pd.read_sql_table("bronze_sales", engine)

# Преобразуем в datetime
sales_df['sales_timestamp'] = pd.to_datetime(sales_df['sales_timestamp'], errors='coerce')

# Заполняем пропуски времени (00:00:00), если дата есть
sales_df['sales_timestamp'] = sales_df['sales_timestamp'].fillna(
    sales_df['sales_timestamp'].dt.floor('D')
)

# Удаляем строки, где дата полностью отсутствует
sales_df = sales_df.dropna(subset=['sales_timestamp'])

# Загружаем в Silver
sales_df.to_sql("silver_sales", engine, if_exists="append", index=False)

print("Данные sales загружены в silver_sales")

# --- 5. Обработка остальных таблиц (загрузка без изменений) ---
print("\nЗагрузка остальных таблиц в Silver...")

tables = {
    #"bronze_countries": "silver_countries",
    #"bronze_cities": "silver_cities",
    #"bronze_categories": "silver_categories",
    #"bronze_products": "silver_products",
    #"bronze_shops": "silver_shops",
    #"bronze_customers": "silver_customers"
}

for bronze, silver in tables.items():
    df = pd.read_sql_table(bronze, engine)
    df.to_sql(
        silver,
        engine,
        if_exists="append",
        index=False,
        schema="silver",
        method="multi"
    )
print("Все данные успешно загружены в Silver-слой!")


