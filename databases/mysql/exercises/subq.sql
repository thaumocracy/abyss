use book_shop;
SELECT * from books where pages=(SELECT MIN(pages) from books);