select MAX(product_id) from products;


INSERT INTO products (product_id, product_name, price, category_id, class, modify_timestamp, resistant, 
is_allergic, vitality_days)
VALUES 
(506, 'Organic Banana Family Pack', 15.99, 1, 'A', NOW(), 'YES', 'NO', 7),
(507, 'Organic Green Apples', 12.50, 1, 'A', NOW(), 'YES', 'NO', 14);


select * from products where product_id in (506, 507);