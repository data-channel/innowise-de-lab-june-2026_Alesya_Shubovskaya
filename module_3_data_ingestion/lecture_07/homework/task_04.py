# Исходные данные, словарь
usd_prices = {
"Banana": 1.2,
"Mango": 2.5,
"Avocado": 2.0
}

# 1. Создание нового словаря
eur_prices = {product: price * 0.9 for product, price in usd_prices.items()}
print(eur_prices)

