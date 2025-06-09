with recursive tmp as(
    
    select id, parent_id, 1 as grade
    from ecoli_data
    where parent_id is null
    
    union all
    
    select d1.id, d1.parent_id, grade + 1 as grade
    from ecoli_data d1
    join tmp t on t.id = d1.parent_id
)
select count(*) count, grade as generation
from tmp t
left join ecoli_data d3 on t.id = d3.parent_id
where d3.id is null 
group by grade
order by grade