update data_layers
set manager_email = 'manager_1@gmail.com'
where layer_name = 'Bronze';


update data_layers
set manager_email = 'manager_2@gmail.com'
where layer_name = 'Silver';


update data_layers
set manager_email = 'manager_3@gmail.com'
where layer_name = 'Gold';


alter table data_layers
add constraint unique_manager_email unique (manager_email);


select * from data_layers;