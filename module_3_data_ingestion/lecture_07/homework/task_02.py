# Входные данные, словарь
product = {
	"id": 105,
	"name": "Organic Buckwheat",
	"price": 3.50,
	"stock": 100
}

# 1. Изменение значения ключа
product["price"] = 4.20
#print(product)

# 2. Добавление нового ключа
product["category"] = "Grains"

# 3. Использование метода .get()
discount_rate = product.get("discount", 0)

# 4. Итоговый отчет
print(product)
print(discount_rate)