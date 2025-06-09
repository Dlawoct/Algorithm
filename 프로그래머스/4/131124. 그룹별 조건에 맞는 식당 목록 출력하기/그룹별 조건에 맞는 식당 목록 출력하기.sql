with tmp as(
    select member_id, count(*) as cnt
    from rest_review
    group by member_id
)
select p.member_name, review_text, date_format(review_date, "%Y-%m-%d") as review_date
from member_profile p
join rest_review r on p.member_id = r.member_id
where p.member_id in (
    select member_id
    from tmp
    WHERE cnt = (SELECT MAX(cnt) FROM tmp)
    )
order by review_date, review_text