with tmp as (
    select product_id, sum(amount) as al
    from food_order
    where produce_date like "2022-05%"
    group by product_id
)
SELECT t.product_id, product_name, (f.price * t.al) as total_sales
from tmp t
join food_product f on t.product_id = f.product_id
order by total_sales desc, t.product_id 