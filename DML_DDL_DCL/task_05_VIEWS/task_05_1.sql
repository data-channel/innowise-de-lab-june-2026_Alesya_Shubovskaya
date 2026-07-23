CREATE OR REPLACE FUNCTION avg_sales_per_employee(p_employee_id INTEGER)
RETURNS DECIMAL
LANGUAGE plpgsql
AS $$
DECLARE
    avg_amount DECIMAL;
BEGIN
    SELECT AVG(total_price)
    INTO avg_amount
    FROM sales
    WHERE employee_id = p_employee_id;
    
    RETURN avg_amount;
END;
$$;


select avg_sales_per_employee(21);