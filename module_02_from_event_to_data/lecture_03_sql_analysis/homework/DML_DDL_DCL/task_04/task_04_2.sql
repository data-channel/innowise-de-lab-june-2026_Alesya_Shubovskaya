delete from employees
where employee_id not in (select distinct employee_id from sales);


select COUNT(*) from employees;