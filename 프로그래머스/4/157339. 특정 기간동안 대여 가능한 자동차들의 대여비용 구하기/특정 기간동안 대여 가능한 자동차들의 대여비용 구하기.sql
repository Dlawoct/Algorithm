WITH unavailable_car AS (
    SELECT car_id
    FROM car_rental_company_rental_history
    WHERE start_date <= '2022-11-30'
      AND end_date >= '2022-11-01'
),
available_car AS (
    SELECT c.car_id, c.car_type, c.daily_fee, p.discount_rate
    FROM car_rental_company_car c
    JOIN car_rental_company_discount_plan p ON c.car_type = p.car_type
    WHERE c.car_type IN ('세단', 'SUV')
      AND p.duration_type = '30일 이상'
      AND c.car_id NOT IN (SELECT car_id FROM unavailable_car)
)
SELECT 
    car_id,
    car_type,
    FLOOR(daily_fee * (1 - CAST(REPLACE(discount_rate, '%', '') AS DECIMAL)/100) * 30) AS fee
FROM available_car
WHERE FLOOR(daily_fee * (1 - CAST(REPLACE(discount_rate, '%', '') AS DECIMAL)/100) * 30)
      BETWEEN 500000 AND 1999999
ORDER BY fee DESC, car_type ASC, car_id DESC;