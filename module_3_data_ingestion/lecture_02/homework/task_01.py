# 1.Инициализация переменных с ошибочными категориями
category_a = "Vegetables"   # Ошибка: должно быть "Fruits"
category_b = "Fruits"       # Ошибка: должно быть "Vegetables"

# Свойства товара
price_per_unit_a = 150  # Цена за ящик партии фруктов
quantity_a = 40  # Количество ящиков партии фруктов
vat_rate = 0.2  # НДС 20%

# 2.Обмен ошибочных значений переменных
category_a, category_b = category_b, category_a

# 3.Расчёт общей стоимости партии товавра
total_value = (price_per_unit_a * quantity_a) + (price_per_unit_a * quantity_a + vat_rate)

# 4.Проверка
print(category_a)
print(category_b)
print(total_value)

