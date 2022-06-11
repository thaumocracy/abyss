use shirts_db;
CREATE TABLE shirts (
  shirt_id INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (shirt_id),
  article VARCHAR(100) NOT NULL,
  color VARCHAR(100) NOT NULL DEFAULT 'white',
  shirt_size VARCHAR(5) NOT NULL,
  last_worn INT NOT NULL DEFAULT 0
)