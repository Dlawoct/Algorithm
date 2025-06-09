with tmp as(
    select animal_id
    from animal_ins
    where sex_upon_intake like "Intact%"
)
SELECT o.animal_id, animal_type, name
from animal_outs o
join tmp t on o.animal_id = t.animal_id
where sex_upon_outcome not like "Intact%"
order by o.animal_id