SELECT
    e.emp_no,
    e.emp_name,
    CASE 
        WHEN g.avg_score >= 96 THEN 'S'
        WHEN g.avg_score >= 90 THEN 'A'
        WHEN g.avg_score >= 80 THEN 'B'
        ELSE 'C'
    END AS GRADE,
    CASE 
        WHEN g.avg_score >= 96 THEN e.sal * 0.2
        WHEN g.avg_score >= 90 THEN e.sal * 0.15
        WHEN g.avg_score >= 80 THEN e.sal * 0.10
        ELSE 0
    END AS BONUS
FROM hr_employees e
JOIN (
    SELECT emp_no, AVG(score) AS avg_score
    FROM hr_grade
    GROUP BY emp_no
) g ON e.emp_no = g.emp_no
ORDER BY e.emp_no;