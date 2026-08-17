select current_user;


select * from sales limit 5;

insert into sales (sale_id)
values (1048576);


select * from sales where sale_id = 1048576;


update sales
set total_price = 300.00
where sale_id = 1048576;


select * from sales where sale_id = 1048576;