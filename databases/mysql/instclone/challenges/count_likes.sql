use instaclone;
SELECT 
    COUNT(*) as likes_count,
    photo_id,
    user_id 
from likes 
    group by photo_id 
    order by likes_count  desc
    limit 5;