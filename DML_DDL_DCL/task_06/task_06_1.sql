select
    e.employee_id,
    e.first_name,
    e.last_name,
    SUM(s.total_price) as total_sales
from employees e
join sales s on e.employee_id = s.employee_id
group by e.employee_id, e.first_name, e.last_name
having SUM(s.total_price) > 1000;