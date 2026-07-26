# 1. Входные данные
product = " фермерский ТВОРОГ "
price = 4.567
qty = 3
csv_row = "milk,bread,cheese"
review = "Это лучший ТВОРОГ в городе!"
file_path = r"C:\EcoMarket\data\2025\january\sales.csv"

# 1. Нормализация названия товара
clean_product = product.strip().lower().title()

# 2. Формирование чека для клиента
total = price * qty
receipt = (
    f'Чек "EcoMarket"\n'
    f"Товар: {clean_product}\n"
    f"Кол-во: {qty}\n"
    f"Итого: {total:.2f} руб."
)
print(receipt)

# 3. Подготовка строки из CSV
csv_items = csv_row.split(",")
csv_combined = " | ".join(csv_items)

print(csv_combined)

# 4. Проверка отзыва клиента
if "творог" in review.lower():
    print(r"Отзыв относится к категории: Dairy C:\EcoMarket\data\2025\january\sales.csv")
print()

# 5. Работа с путём к файлу
file_path = r"C:\EcoMarket\data\2025\january\sales.csv"

# r'' перед строкой используется, чтобы обратные слеши \\ не интерпретировались как управляющие символы