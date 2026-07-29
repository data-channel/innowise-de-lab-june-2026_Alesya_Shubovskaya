# Глобальная переменная
SMALL_BATCH_LIMIT = 500

# Описание функции
def calculate_batch(weight, price, discount=0.0):
    """
    Рассчитывает общую стоимость партии товара с учётом скидки.

    Параметры:
    weight — вес партии в кг (число)
    price — цена за один кг (число)
    discount — процент скидки (от 0 до 100). По умолчанию 0.0.

    Возвращает:
    Итоговая стоимость партии после применения скидки (число)
    """
    final_sum = weight * price * (1 - discount)
    is_limit_exceeded = final_sum > SMALL_BATCH_LIMIT
    return(final_sum, is_limit_exceeded)

# Вызов функции (морковь)
carrot_sum, carrot_exceeded = calculate_batch(100, 4)

# Вызов функции (яблоки)
apple_sum, apple_exceeded = calculate_batch(50, 20)

# Итоговый отчет
print(f"Партия 1 (Морковь): {carrot_sum, carrot_exceeded}")
print(f"Партия 2 (Яблоки): {apple_sum, apple_exceeded}")

