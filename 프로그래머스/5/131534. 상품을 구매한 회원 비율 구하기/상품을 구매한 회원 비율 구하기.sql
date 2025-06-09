with tmp as(
SELECT online_sale_id, s.user_id, product_id, sales_amount, sales_date
from user_info i
join online_sale s on i.user_id = s.user_id
where joined like "2021%"
)
select 
    year(sales_date) as YEAR, 
    month(sales_date) as MONTH,
    count(distinct user_id) as purchased_users,
    round(count(distinct user_id) / (select count(*) from user_info where joined like "2021%"), 1) as purchased_ratio
from tmp
group by YEAR, MONTH
order by YEAR, MONTH
