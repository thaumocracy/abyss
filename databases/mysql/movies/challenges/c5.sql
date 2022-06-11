use movies;
SELECT 
    genre,
    LPAD(AVG(rating),7,0) as avg_rating
FROM series
INNER JOIN reviews
    on series.id = reviews.series_id
    GROUP BY genre;
