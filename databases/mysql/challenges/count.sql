USE book_shop;
-- SELECT COUNT(*) FROM books;
-- SELECT released_year,COUNT(*) FROM BOOKS AS year GROUP BY released_year;
-- SELECT SUM(stock_quantity) FROM BOOKS;
-- SELECT CONCAT(author_fname,' ',author_lname) as author, AVG(released_year)  as avg_year FROM BOOKS GROUP BY author_lname,author_fname;
-- SELECT CONCAT(author_fname,' ',author_lname) as full_name, title FROM books ORDER BY LENGTH(title) DESC;
-- SELECT released_year as year,count(*),AVG(pages) from books GROUP BY released_year;