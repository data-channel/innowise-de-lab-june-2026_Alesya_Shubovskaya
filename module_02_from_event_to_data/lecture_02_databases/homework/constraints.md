## Шаг 3. Добавление ограничений (Constraints)
### NOT NULL (обязательные поля)
- Sales.sales_id — первичный ключ.
- Sales.product_id — без товара продажа невозможна.
- Sales.quantity — количество обязательно.
- Sales.total_price — цена должна быть известна.
- Products.product_id — первичный ключ.
- Products.product_name — название товара обязательно.
- Products.price — цена обязательна.

### UNIQUE (уникальные поля)
- Sales.transaction_number — номер чека должен быть уникальным.
- Products.product_name — название товара уникально.
- Customers.email — email уникален.
- Categories.category_name — название категории уникально.

### CHECK (проверка значений)
- Sales.quantity > 0 — количество не может быть меньше или равно 0.
- Sales.total_price >= 0 — цена не может быть отрицательной.
- Sales.discount >= 0 AND discount <= total_price — скидка не может быть больше цены.
- Products.price >= 0 — цена не может быть отрицательной.
- Employees.birth_date < hire_date — дата рождения должна быть раньше даты найма.

