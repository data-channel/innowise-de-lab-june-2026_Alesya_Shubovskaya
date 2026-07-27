# 1. Инициализация списка
prices = [100, -50, 300, 40, 800]

# 2. Очистка данных
prices.remove(-50)
#print(prices)

#3. Изменение списка
prices.append(150)
#print(prices)

# 4. Сортировка списка
prices.sort()
#print(prices)

# 5. Создание нового списка через List Comprehension
tax_prices = [x * 1.2 for x in prices if x * 1.2 > 100]
#print(tax_prices)

# 6. Вывод в консоль
print(f"Базовый прайс (очищенный): {prices}")
print(f"Цены с НДС (>100): {tax_prices}")
print(f"Общая выручка: {sum(tax_prices)}")
print(f"Минимум: {min(tax_prices)}")
print(f"Максимум: {max(tax_prices)}")

