-- 코드를 입력하세요
SELECT a.author_id, author_name, category, sum((price * sales)) as total_sales
from author a
join book b on a.author_id = b.author_id
join book_sales bs on b.book_id = bs.book_id
where sales_date like "2022-01%"
group by author_id, category
order by author_id, category desc
