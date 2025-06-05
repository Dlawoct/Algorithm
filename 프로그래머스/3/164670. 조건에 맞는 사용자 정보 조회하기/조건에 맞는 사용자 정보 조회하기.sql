-- 코드를 입력하세요
SELECT distinct
    user_id, 
    nickname, 
    concat(city," ",street_address1," ",street_address2) 전체주소,
    concat(SUBSTRING(u.TLNO,1,3), '-', SUBSTRING(u.TLNO,4,4), '-', SUBSTRING(u.TLNO,8,4)) AS 전화번호
from used_goods_user u
join used_goods_board b on u.user_id = b.writer_id
where user_id in (select writer_id
                  from used_goods_board
                  group by writer_id
                  having count(writer_id) >= 3
                 )
order by user_id desc