use book_shop;

SELECT CONCAT(SUBSTRING(title,1,5),'...') AS short_title FROM BOOKS;