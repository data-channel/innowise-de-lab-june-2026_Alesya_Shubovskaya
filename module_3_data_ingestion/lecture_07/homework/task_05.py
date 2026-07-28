# Входные данные
import json
api_response_json = """ 
{ 
	"store": "StoreHub", 
	"orders": [ 
		{"id": 1, "total": 50}, 
		{"id": 2, "total": 200}, 
		{"id": 3, "total": 150} 
		]
 } 
"""

# 1. Десериализация
api_response = json.loads(api_response_json)
#print(api_response)

# 2. Список заказов по ключу
orders = api_response["orders"]
#print(orders)

# 3. Формирование нового списка
high_value_orders = [order for order in orders if order["total"] > 100]
#print(high_value_orders)

# 4. Добавление списка обратно в словарь
api_response["high_value_orders"] = high_value_orders

# 5. Сериализация
new_json = json.dumps(api_response, indent=2)
print(new_json)