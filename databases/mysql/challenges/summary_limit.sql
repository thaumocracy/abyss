use book_shop;
SELECT
    CONCAT(SUBSTRING(title,1,10),'...') as short_title,
    CONCAT(author_lname,',',author_fname) as author,
    CONCAT(stock_quantity,' in stock') as quantity from books;
    

