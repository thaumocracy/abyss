USE instaclone;

CREATE TABLE users(
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO users(username) VALUES 
('BantikTheCat'),
('Arshe Hoole'),
('Thaumo Cracy')
