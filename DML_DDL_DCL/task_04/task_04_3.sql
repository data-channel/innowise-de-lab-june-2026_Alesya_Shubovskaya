BEGIN;

INSERT INTO employees (employee_id, first_name, middle_initial, last_name, shop_id)
VALUES (327, 'Mark', 'C', 'Popovich', 1);

INSERT INTO sales (sale_id, employee_id, product_id, total_price, sales_timestamp)
VALUES (1048577, 327, 1, 100.00, NOW());

COMMIT;



SELECT * FROM employees WHERE employee_id = 327;
SELECT * FROM sales WHERE sale_id = 1048577;