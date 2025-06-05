-- 코드를 입력하세요
SELECT year(sales_date) as year, month(sales_date) as month, gender, count(distinct o.user_id)users
from online_sale o
join user_info i on o.user_id = i.user_id
where gender is not null
group by year, month, gender
order by year, month, gender