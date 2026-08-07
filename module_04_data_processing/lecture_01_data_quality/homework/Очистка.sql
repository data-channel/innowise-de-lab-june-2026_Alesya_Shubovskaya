delete from silver.silver_employees
where employee_id IN (
    select employee_id
    from silver.silver_employees
    group by employee_id
    having count(*) > 1
)
and ctid not in (
    select min(ctid)
    from silver.silver_employees
    group by employee_id
    having count(*) > 1
);

delete from silver.silver_employees
where employee_id is null;

delete from silver.silver_employees
where not exists (
    select 1
    from silver.silver_sales
    where silver.silver_sales.employee_id = silver.silver_employees.employee_id 
)