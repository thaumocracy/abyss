use instaclone;

SELECT 
    count(*) AS total,
    user_id
FROM likes
INNER JOIN users 
    on likes.user_id = users.id 
    GROUP BY user_id 
    HAVING total=(SELECT COUNT(*) FROM photos);

