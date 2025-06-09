-- 코드를 작성해주세요
with tmp as(
    select sum(code) as fc
    from skillcodes
    where category = "Front End"
    group by category
)
select id, email, first_name, last_name
from developers d
where (skill_code & (select fc from tmp)) > 0
order by id 