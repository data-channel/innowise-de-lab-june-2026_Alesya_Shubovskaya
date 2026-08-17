## Шаг 4. Физическая ER-диаграмма
### Сущность Countries
- country_id (PK, INT, NOT NULL)
- country_name (VARCHAR(100), NOT NULL, UNIQUE)
- country_code (VARCHAR(2), NOT NULL, UNIQUE)

### Сущность Cities
- city_id (PK, INT, NOT NULL)
- city_name (VARCHAR(100), NOT NULL)
- zipcode (VARCHAR(10), NOT NULL)
- country_id (FK → Countries, INT)

### Сущность Shops
- shop_id (PK, INT, NOT NULL)
- address (VARCHAR(255), NOT NULL)
- city_id (FK → Cities, INT)

### Сущность Employees
- employee_id (PK, INT, NOT NULL)
- first_name (VARCHAR(100), NOT NULL)
- middle_initial (CHAR(1))
- last_name (VARCHAR(100), NOT NULL)
- birth_date (DATE, NOT NULL)
- gender (CHAR(1), CHECK gender IN ('M', 'F'))
- hire_date (DATE, NOT NULL)
- shop_id (FK → Shops, INT)
- city_id (FK → Cities, INT)
- hire_date (DATE, NOT NULL)
- 
### Сущность Customers
- customer_id (PK, INT, NOT NULL)
- first_name (VARCHAR(100), NOT NULL)
- middle_initial (CHAR(1))
- last_name (VARCHAR(100), NOT NULL)
- city_id (FK → Cities, INT)
- address (VARCHAR(255), NOT NULL)

### Сущность Categories
- category_id (PK, INT, NOT NULL)
- category_name (VARCHAR(100), NOT NULL, UNIQUE)

### Сущность Products
- product_id (PK, INT, NOT NULL)
- product_name (VARCHAR(255), NOT NULL, UNIQUE)
- price (DECIMAL(10,2), NOT NULL, CHECK price >= 0)
- category_id (FK → Categories, INT)
- class (VARCHAR(50)
- modify_timestamp (TIMESTAMP)
- resistant (BOOLEAN)
- is_allergic (BOOLEAN)
- vitality_days (INT, CHECK (vitality_daays >=0)

### Сущность Sales
- sales_id (PK, INT, NOT NULL)
- product_id (FK → Products, INT, NOT NULL)
- customer_id (FK → Customers, INT)
- employee_id (FK → Employees, INT)
- shop_id (FK → Shops, INT)
- quantity (INT, NOT NULL, CHECK quantity > 0)
- discount (DECIMAL(10,2), CHECK discount >= 0 AND discount <= total_price)
- total_price (DECIMAL(10,2), NOT NULL, CHECK total_price >= 0)
- sales_timestamp (TIMESTAMP)
- transaction_number (VARCHAR(50), UNIQUE)


## Связи между таблицами
- Countries (1) → Cities (M)
- Cities (1) → Shops (M)
- Cities (1) → Employees (M)
- Cities (1) → Customers (M)
- Shops (1) → Employees (M)
- Shops (1) → Sales (M)
- Employees (1) → Sales (M)
- Customers (1) → Sales (M)
- Products (1) → Sales (M)
- Categories (1) → Products (M)
