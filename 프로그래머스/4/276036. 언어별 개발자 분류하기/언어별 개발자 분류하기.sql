with tmp1
as (
    select 
        (select sum(code) from skillcodes where category = "Front End") as frontend,
        (select sum(code) from skillcodes where name = "Python") as python,
        (select sum(code) from skillcodes where name = "C#") as cshop
), tmp2
as (
    select 
    case
        when skill_code & t.frontend > 0 and skill_code & t.python > 0 then 'A'
        when skill_code & t.cshop > 0 then 'B'
        when skill_code & t.frontend > 0 then 'C'
    end as grade, id, email
    from developers, tmp1 t
)
select *
from tmp2
where grade is not null
order by grade, id
