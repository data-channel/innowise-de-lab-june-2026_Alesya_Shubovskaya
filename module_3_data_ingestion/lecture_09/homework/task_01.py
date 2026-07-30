def calculate_purchase(product_name, weight, price):
    """
    Рассчитывает стоимость партии товара и технический индекс.

    Параметры:
    product_name (str) — название товара
    weight — вес партии (может быть числом, строкой или другим типом)
    price (float) — цена за кг

    Возвращает: None (всё выводится на экран)
    """
    try:
        # 1. Пытаемся преобразовать вес в число
        numeric_weight = float(weight)

        # 2. Рассчитываем полную стоимость
        total_cost = numeric_weight * price

        # 3. Рассчитываем индекс распределения
        technical_index = 100 / numeric_weight

        # 4. Если всё прошло — выводим результат
        print(f"Товар: {product_name}. Итоговая стоимость: {total_cost}$")
        print(f"Технический индекс: {technical_index}")

    except TypeError as e:
        print(f"Тип ошибки: {type(e)}")

    except ValueError as e:
        print(f"Тип ошибки: {type(e)}")

    except ZeroDivisionError as e:
        print(f"Тип ошибки: {type(e)}")

    finally:
        print("--- Проверка партии завершена ---\n")


# --- Тестовые вызовы ---
# Корректные данные
calculate_purchase("Томаты", 100, 2.5)

# С ошибкой типа данных
calculate_purchase("Огурцы", "пятьдесят", 1.8)

# 3. Ошибка деления на ноль
calculate_purchase("Перец", 0, 4)

# 4. Ошибка типа данных (список вместо числа)
calculate_purchase("Зелень", [10], 5)