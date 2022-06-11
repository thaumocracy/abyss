use movies;

SELECT 
    title, 
    LPAD(AVG(rating),7,0) as rating
FROM series
JOIN reviews
    ON series.id = reviews.series_id
    GROUP BY series.id
    ORDER BY AVG(rating) ASC;