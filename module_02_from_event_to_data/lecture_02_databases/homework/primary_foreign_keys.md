Первичные ключи (Primary Keys)

1. Sales → sales_id (уникальный номер продажи)
2. Products → product_id (уникальный номер товара)
3. Employees → employee_id (уникальный номер сотрудника)
4. Customers → customer_id (уникальный номер клиента)
5. Shops → shop_id (уникальный номер магазина)
6. Categories → category_id (уникальный номер категории)
7. Cities → city_id (уникальный номер города)
8. Countries → country_id (уникальный номер страны)

Обоснование (на примере customers и categories):
· Customers – первичным ключом выбран customer_id, потому что каждый клиент имеет уникальный идентификатор, 
который не повторяется и не меняется.
· Categories – первичным ключом выбран category_id, потому что каждая категория товаров имеет свой уникальный номер, 
который однозначно её идентифицирует.

Внешние ключи (Foreign Keys)

1. Sales содержит внешние ключи:
   · product_id → ссылается на Products(product_id)
   · customer_id → ссылается на Customers(customer_id)
   · employee_id → ссылается на Employees(employee_id)
   · shop_id → ссылается на Shops(shop_id)
2. Employees содержит внешний ключ:
   · shop_id → ссылается на Shops(shop_id)
   · city_id → ссылается на Cities(city_id)
3. Customers содержит внешний ключ:
   · city_id → ссылается на Cities(city_id)
4. Shops содержит внешний ключ:
   · city_id → ссылается на Cities(city_id)
5. Products содержит внешний ключ:
   · category_id → ссылается на Categories(category_id)
6. Cities содержит внешний ключ:
   · country_id → ссылается на Countries(country_id)

Описание связей между сущностями и их кратности
1. Sales и Products → M:1 (многие к одному)
Объяснение: Один товар (product_id) может встречаться во множестве продаж, но каждая продажа относится только к одному товару.
2. Employees и Cities → M:1 (многие к одному)
Объяснение: Множество сотрудников могут проживать в одном городе, но один сотрудник живёт только в одном городе.
3. Cities и Countries → M:1 (многие к одному)
Объяснение: В одной стране может быть много городов, но каждый город находится только в одной стране.


---
