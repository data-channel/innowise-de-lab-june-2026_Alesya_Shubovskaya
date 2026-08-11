# Кросс-фильтрация

CREATE OR REPLACE VIEW mart.mart_location_slicer AS
SELECT DISTINCT
    city_name AS city,
    country_name AS country
FROM gold.dim_location
WHERE city_name IS NOT NULL AND country_name IS NOT NULL
ORDER BY country_name, city_name;

SELECT * FROM mart.mart_location_slicer ORDER BY country, city;