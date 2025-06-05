with recursive temp(hour, count)
as(
    select 0, (select count(*) from animal_outs where hour(datetime) = 0)
    
    union all
    
    select t.hour + 1, (select count(*) from animal_outs where hour(datetime) = t.hour + 1)
    from temp t
    where t.hour < 23
)
select *
from temp