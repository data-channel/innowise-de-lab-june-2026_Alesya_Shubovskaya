# 1. Создание родительского класса
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.__price = price    # приватный атрибут (инкапсуляция)

    # Getter для price
    def get_price(self):
        """Возвращает текущее значение __price"""
        return self.__price

    # Setter для price
    def set_price(self, new_price: float):
        """Устанавливает новую цену, если она больше 0"""
        if new_price > 0:
            self.__price = new_price
        else:
            print(f"Ошибка безопасности:Цена должна быть положительной!")

    def calculate_cost(self):
        """Для базового товара стоимость равна его цене"""
        return self.get_price()

    def get_display_info(self):
        """Возвращает строку с информацией о товаре"""
        return f"Товар: [{self.name}] | Цена: [{self.get_price()}] руб."


# 2. Создаём дочерний класс WeighableProduct
class WeighableProduct(Product):
    def __init__(self, name: str, price: float, weight: float):
        super().__init__(name, price)      # Вызываем __init__ родительского класса Product
        self._weight = weight              # Принимаем новый атрибут

    def calculate_cost(self):
        """Стоимость = цена * вес"""
        return self.get_price() * self._weight

    def get_display_info(self):
        """Возвращает строку для чека"""
        return f"Весовой товар: [{self.name}] | Вес: [{self._weight}] кг. | Итого: [{self.calculate_cost()}] руб."

# 3. Создаём дочерний класс PackagedProduct
class PackagedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price)    # Вызываем __init__ родительского класса Product
        self.quantity = quantity         # Принимаем новый атрибут

    def calculate_cost(self):
        """Стоимость = цена * количество"""
        return self.get_price() * self.quantity

    def get_display_info(self):
        """Возвращает строку для чека"""
        return f"Упаковка: [{self.name}] | Количество: [{self.quantity}] шт. | Итого: [{self.calculate_cost()}] руб."

# 4. Стимуляция работы кассы
# Создание пустой корзины
cart = []

# 2. Добавляем товары
cart.append(Product("Молоко", 100))                # базовый товар
cart.append(WeighableProduct("Яблоки", 50, 2.5))      # весовой товар
cart.append(PackagedProduct("Яйца", 12, 10))        # товар в упаковке

# 3. Попытка взлома (установить отрицательную цену)
cart[0].set_price(-200)   # Молоко — попытка установить цену -200

# 4. Проходим по корзине и выводим информацию о каждом товаре
print("\n--- Чек EcoMarket ---")
print(cart[0].get_display_info())
for item in cart:
    print(item.get_display_info())
print("-------------------------")

# 5. Считаем общую сумму
total = sum(item.calculate_cost() for item in cart)
print(f"ИТОГО К ОПЛАТЕ: {total} руб.")










