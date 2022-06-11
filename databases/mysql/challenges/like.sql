use book_shop;
-- SELECT * FROM BOOKS WHERE title LIKE '%stories%';
-- SELECT * FROM BOOKS ORDER BY pages DESC LIMIT 1 ;
-- SELECT CONCAT(title,'-',released_year) as summary FROM BOOKS  ORDER BY released_year DESC LIMIT 3 ;
-- SELECT * FROM BOOKS WHERE author_lname LIKE '% %';
-- SELECT title, released_year , stock_quantity FROM BOOKS ORDER BY stock_quantity LIMIT 3;
-- SELECT title,author_lname from BOOKS ORDER BY author_lname,title
SELECT CONCAT('THIS IS CONCAT >',UPPER(author_fname),' ',UPPER(author_lname),'< SORTED')  as yell FROM BOOKS ORDER BY author_lname;