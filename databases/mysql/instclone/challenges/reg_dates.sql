use instaclone;
SELECT 
    COUNT(*) as total,
    DAYNAME(created_at) as day
from users 
    GROUP BY day
    ORDER BY total DESC;