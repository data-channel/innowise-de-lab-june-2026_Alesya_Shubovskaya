alter table silver.silver_employees
add constraint check_hire_after_birth
check (hire_date > birth_date);


select constraint_name, constraint_type
from information_schema.table_constraints
where table_name = 'silver_employees' and table_schema = 'silver';

