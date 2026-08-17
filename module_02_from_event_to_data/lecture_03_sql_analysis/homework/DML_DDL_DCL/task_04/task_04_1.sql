update products
set price = price * 1.10
from categories
where products.category_id = categories.category_id
   and categories.category_name = 'Fruits';


SELECT p.product_name, p.price, c.category_name
FROM products p
JOIN categories c ON p.category_id = c.category_id
WHERE c.category_name = 'Fruits';


