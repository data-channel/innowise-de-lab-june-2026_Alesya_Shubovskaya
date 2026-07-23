create table data_layers (
    layer_id SERIAL primary key,
    layer_name VARCHAR(50) unique not null,
    description TEXT
);







