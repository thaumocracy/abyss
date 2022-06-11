use list_app;
CREATE TABLE Books
(
  id INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (id),
  title VARCHAR(200) NOT NULL DEFAULT 'Update title pls',
  author VARCHAR(200) NOT NULL DEFAULT 'Update author pls',
  image VARCHAR(1000) NOT NULL DEFAULT 'Update image link pls',
  finished BOOLEAN NOT NULL DEFAULT FALSE,
  description VARCHAR(2000) NOT NULL DEFAULT 'Update description pls'
)