use instaclone;

select 
    count(*),
    tag_id,
    tag_name
from photo_tags
INNER JOIN tags 
        ON tag_id = tags.id
    group by tag_id 
    order by count(*) desc 
    limit 5;