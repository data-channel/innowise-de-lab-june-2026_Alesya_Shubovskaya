update silver.silver_sales
set
    shop_id = e.city_id,
    city_id = e.shop_id
from silver.silver_employees e
where silver.silver_sales.employee_id = e.employee_id;


select sales_id, employee_id, shop_id, city_id
from silver.silver_sales
limit 10;
    
    
    