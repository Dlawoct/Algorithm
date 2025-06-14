select d.dept_id, dept_name_en, round(avg(sal)) as avg_sal
from hr_department d
join hr_employees e on d.dept_id = e.dept_id
group by d.dept_id
order by avg_sal desc