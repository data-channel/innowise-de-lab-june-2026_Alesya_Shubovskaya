select
    sh.shop_id,
    sh.address,
    c.city_name,
    co.country_name
from shops sh
join cities c on sh.city_id = c.city_id
join countries co on c.country_id = co.country_id
where co.country_name = 'Poland';




