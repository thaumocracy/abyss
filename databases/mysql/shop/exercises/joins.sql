SELECT 
    first_name,
    title,
    grade
from students
LEFT JOIN papers
    on students.id = papers.student_id;


SELECT 
    IFNULL(first_name,'MISSING'),
    title,
    IFNULL(AVG(grade),0)
from students
LEFT JOIN papers
    on students.id = papers.student_id
GROUP BY students.id;

SELECT 
    IFNULL(first_name,'MISSING'),
    title,
    IFNULL(AVG(grade),0),
    CASE
        WHEN AVG(grade) > 75 THEN 'PASSING'
        ELSE 'FAILED'
    END
from students
LEFT JOIN papers
    on students.id = papers.student_id
GROUP BY students.id
ORDER BY AVG(grade) DESC;