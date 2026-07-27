# 1.Инициализация данных
rows_range = range(1, 6)
rows = list(rows_range)
#print(rows)

# 2. Изменение по индексу
rows[2] = "Ремонт"
#print(rows)

# 3. Проверка наличия значения
if 5 in rows:
    print(f"Ряд 5 доступен")

# 4. Выполнение среза
priority_rows = rows[:3]
print(priority_rows)

# 5. Вывод в консоль
print(f"Список рядов: {rows}")
print(f"Приоритетные ряды: {priority_rows}")
