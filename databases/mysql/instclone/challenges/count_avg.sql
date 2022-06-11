use instaclone;

SELECT (
    (SELECT COUNT(*) FROM photos) / (SELECT COUNT(*) FROM users)
) as average_per_user;