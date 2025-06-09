-- 코드를 입력하세요
SELECT j.flavor
from first_half f
right outer join july j on f.shipment_id = j.shipment_id
group by flavor
order by (f.total_order + sum(j.total_order)) desc
limit 3