# 1. Входные данные
raw_log = "ORDER-2025-01-15|FRT-APPLE-PL|+111 (23) 456-78-90| мИНсК "

# 2. Разделяем строку по разделителю "|"
order_id, product_code, raw_phone, raw_city = raw_log.split("|")

# print(f"Заказ: {order_id}")
# print(f"Код товара: {product_code}")
# print(f"Телефон (сырой): {raw_phone}")
# print(f"Город (сырой): {raw_city}\n")

# 3. Разбираем код товара
# 3.1 Первые 3 символа — категория
category = product_code[:3]

# print(category)

# 3.2 Последние 2 символа — регион (отрицательная индексация)
region = product_code[-2:]

# print(region)

# 3.3 Позиция первого дефиса
first_dash_pos = product_code.find("-")

print(f"Позиция первого дефиса в коде товара: {first_dash_pos}")

# 3.4 Проверка, начинается ли код с "FRT"
startswith_frt = product_code.startswith("FRT")

if startswith_frt:
    print("Код товара начинается с 'FRT'")
else:
    print("Код товара не начинается с 'FRT'")
# print()

# 4. Очистка телефона (оставляем только цифры)
clean_phone = ""
for char in raw_phone:
    if char.isdigit():
        clean_phone += char

# print(clean_phone)
print(f"Длина номера: {len(clean_phone)}")

# 5. Приведение города к нормальному виду
clean_city = raw_city.strip().lower().title()

# print(clean_city)

# 6. Формирование итогового отчёта
report = (
    f"Заказ: {order_id}\n"
    f"Категория: {category} | Регион: {region}\n"
    f"Телефон: {clean_phone}\n"
    f"Город: {clean_city}"
)
print(report)