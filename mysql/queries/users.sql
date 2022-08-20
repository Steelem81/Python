INSERT INTO USERS (last_name, first_name, email) VALUES('Steele', 'Jeff', 'steelem81@gmail.com'), ('Richards', 'Denise', 'classy@gmail.com'), ('Reeves', 'Keanu', 'iknowkungfu@hotmail.com');	

SELECT * FROM USERS;

SELECT * FROM USERS WHERE email = 'steelem81@gmail.com';

SELECT * FROM USERS WHERE id = 3;

UPDATE USERS SET last_name = 'Pancakes' WHERE id = 3;

DELETE FROM USERS WHERE id = 2;

SELECT * FROM USERS ORDER BY first_name;

SELECT * FROM USERS ORDER BY first_name DESC;
