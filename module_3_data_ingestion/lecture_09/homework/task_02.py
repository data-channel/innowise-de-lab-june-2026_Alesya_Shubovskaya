from typing import Optional

def calculate_total_delivery_cost(
    product_name: str,
    weights: list[float] | tuple[float, ...],
    prices: list[float] | tuple[float, ...],
    discount: Optional[float] = None,
    currency_rate: float = 1.0,
    *extra_costs: float
) -> dict[str, float]:

    total_sum: float = 0.0
    extra_sum: float = 0.0
    final_sum: float = 0.0

    # 1. Проверить, что количество элементов в weights и prices совпадает
    if len(weights) != len(prices):
        print("Ошибка: количество весов и цен не совпадает")
        return {"Ошибка: -1.0"}

    # 2. Рассчитать стоимость каждой позиции как weight * price
    for i in range(len(weights)):
        total_sum += weights[i] * prices[i]

    # 3. Сложить все стоимости в переменную total_sum (уже сделано)

    # 4. Если discount не None, применить скидку
    if discount is not None:
        total_sum *= (1 - discount)

    # 5. Добавить все значения из extra_costs к итоговой сумме
    extra_sum = sum(extra_costs)
    total_sum += extra_sum

    # 6. Умножить итог на currency_rate
    final_sum = total_sum * currency_rate

    # 7. Вернуть словарь
    return {product_name: final_sum}

result1 = calculate_total_delivery_cost(
    "Товар: Овощная партия, итоговая стоимость:",   # product_name
    [100, 50],          # weights
    [4, 6],             # prices
    0.1,                # discount
    1.0,                # currency_rate
    20, 15              # extra_costs — просто числа
)

result2 = calculate_total_delivery_cost(
    "Товар: Фруктовая партия, итоговая стоимость:", # product_name
    (30, 20, 10),       # weights
    (15, 12, 18),       # prices
    None,               # discount
    1.2,                # currency_rate
    25                  # extra_costs — одно число
)

print(result1)
print(result2)