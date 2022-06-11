use movies;
SELECT first_name,
        last_name,
        IFNULL(MIN(rating),0) AS min,
        IFNULL(MAX(rating),0) AS max,
        IFNULL(LPAD(AVG(rating),7,0),0) as average,
        COUNT(rating) as count,
        IF(COUNT(rating) >= 1 , 'Active', 'Inactive') as status
FROM reviewers
LEFT JOIN reviews 
    ON reviewers.id = reviews.reviewer_id
    GROUP BY reviewers.id; 