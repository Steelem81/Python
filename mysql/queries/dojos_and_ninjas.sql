INSERT INTO dojos (name) VALUES ('Crane'), ('Tiger'), ('Panda');

SET SQL_SAFE_UPDATES = 0;
DELETE FROM dojos;

INSERT INTO dojos (name) VALUES('Marvel'), ('DC'), ('DarkHorse');

INSERT INTO ninjas (first_name, last_name, age, dojo_id) 
VALUES ('Charles', 'Xavier', 52, 4)
		,('Steve', 'Rogers', 93, 4)
        ,('Stephen', 'Strange', 42, 4)
        ,('Bruce', 'Wayne', 35, 5)
        ,('Clark', 'Kent', 84, 5)
        ,('Harleen', 'Quinzel', 31, 5)
        ,('Miyamoto', 'Usagi', 62, 6)
        ,('Hunter', 'Rose', 28, 6)
        ,('Anung', 'un Rama', 800, 6);

SELECT * FROM ninjas INNER JOIN dojos ON ninjas.dojo_id = dojos.id WHERE dojos.name = 'Marvel';
SELECT * FROM ninjas INNER JOIN dojos ON ninjas.dojo_id = dojos.id WHERE dojos.name = 'DC';
SELECT * FROM ninjas INNER JOIN dojos ON ninjas.dojo_id = dojos.id WHERE dojos.name = 'DarkHorse';
SELECT dojos.name FROM ninjas INNER JOIN dojos ON ninjas.dojo_id = dojos.id ORDER BY ninjas.id DESC LIMIT 1;
