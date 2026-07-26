# Инициализация входных данных
product_name = "Морковь мытая"
price = 2.5
stock_quantity = 150
is_local_farm = True
supplier = None

has_coupon = True
has_card = False
total = 10  # Сумма покупки

# Расчёт товара-хита по правилу
is_hit = (price < 3) and is_local_farm

print(f"Является ли товар хитом?: {is_hit}")

# Проверка: есть ли поставщик
has_supplier = supplier is not None
print(f"Поставщик указан?: {has_supplier}")

# Проверка: можно показывать в приложении (есть поставщик И товар в наличии)
can_show_in_app = has_supplier and (stock_quantity > 0)
print(f"Можно показывать в приложении?: {can_show_in_app}")

# Проверка: нужно пополнение (остаток <= 20 ИЛИ товар хит)
needs_restock = (stock_quantity <= 20) or is_hit
print(F"Нужно пополнение?: {needs_restock}")

# Проверка: товар заблокирован (НЕ от местного фермера)
is_blocked = not is_local_farm
print(F"Товар заблокирован?: {is_blocked}")

# Проверка приоритетов операторов без скобок
discount_without_brackets = has_coupon or has_card and total > 50
print(f"Скидка без скобок: {discount_without_brackets}")

# Проверка приоритетов операторов со скобками
discount_with_brackets = (has_coupon or has_card) and total > 50
print(f"Скидка со скобками: {discount_with_brackets}")

# Увеличить цену на 1.0
price += 1.0
print(f"Цена после изменения: {price}")

# Увеличить количество на складе в 2 раза
stock_quantity *= 2
print(F"Остаток после измненения: {stock_quantity}")

# Вычислить число полных коробок по 10 кг
boxes = stock_quantity
boxes //= 10
print(f"Полных коробок по 10 кг: {boxes}")

# Повторный расчёт is_hit и needs_restock
is_hit = (price < 3) and is_local_farm
print(f"Является ли товар хитом (после изменений)?: {is_hit}")
needs_restock = (stock_quantity <= 20) or is_hit
print(f"Нужно ли пополнение (после изменений)?: {needs_restock}")


