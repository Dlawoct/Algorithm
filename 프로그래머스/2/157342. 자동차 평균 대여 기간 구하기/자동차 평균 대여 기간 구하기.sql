select car_id, round(avg(duration), 1) as average_duration
from ( 
    select car_id, timestampdiff(DAY, start_date, end_date) + 1 as duration
    from car_rental_company_rental_history
)as tmp
group by car_id 
having average_duration >= 7
order by average_duration desc, car_id desc