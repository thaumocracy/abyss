use join_us;

-- SELECT 
--     DATE_FORMAT(MIN(created_at)," %M %D %Y") as earliest_date 

-- FROM users;


-- SELECT  * FROM users WHERE created_at = (SELECT MIN(created_at) from users);

-- SELECT 
--     count(*), 
--     MONTHNAME(created_at) as month 
-- FROM users 
--     GROUP BY month 
--     ORDER BY month 
-- DESC;


SELECT 
    CASE
        WHEN email LIKE '%@yahoo.com%' THEN 'yahoo'
        WHEN email LIKE '%@gmail.com%' THEN 'gmail'
        WHEN email LIKE '%@hotmail.com%' THEN 'hotmail'
    ELSE 'other'
    END as provider,
    COUNT(*)
FROM users
GROUP BY provider;