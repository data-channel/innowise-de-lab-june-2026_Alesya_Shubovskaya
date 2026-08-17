select
    co.country_name,
    count(sh.shop_id) as shop_count
from shops sh
join cities c on sh.city_id = c.city_id 
join countries co on c.country_id = co.country_id
group by co.country_name order by shop_count desc;