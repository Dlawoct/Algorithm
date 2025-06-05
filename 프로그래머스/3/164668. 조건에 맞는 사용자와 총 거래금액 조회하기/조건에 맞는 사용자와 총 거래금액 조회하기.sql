-- 코드를 입력하세요
SELECT user_id, nickname, sum(price) total_price
from used_goods_board ugb
join used_goods_user ugu on ugb.writer_id = ugu.user_id
where status = "DONE"
group by user_id
having sum(price) >= 700000
order by sum(price)