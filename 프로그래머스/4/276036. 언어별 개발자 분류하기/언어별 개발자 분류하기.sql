with skill as(
    select
        (select sum(code) from skillcodes where category = "Front End") as front,
        (select sum(code) from skillcodes where name = "Python") as py,
        (select sum(code) from skillcodes where name = "C#") as Cshrp
 ), tmp as (
    select
    case 
        when skill_code & front > 0 and skill_code & py > 0 then 'A'
        when skill_code & Cshrp > 0 then 'B'
        when skill_code & front > 0 then 'C'
     end as GRADE,
     id, email
    from developers d, skill s
 )
 select *
from tmp
where grade is not null
order by grade, id