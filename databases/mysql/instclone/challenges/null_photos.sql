use instaclone;
SELECT username
FROM photos 
    RIGHT JOIN users 
        ON users.id = photos.user_id 
        WHERE photos.id IS NULL;