SET SQL_SAFE_UPDATES = 0;

INSERT INTO dojos (name) values ('Dojo1');
INSERT INTO dojos (name) values ('Dojo2');
INSERT INTO dojos (name) values ('Dojo3');
DELETE FROM dojos;
INSERT INTO dojos (name) values ('Dojo1');
INSERT INTO dojos (name) values ('Dojo2');
INSERT INTO dojos (name) values ('Dojo3');

select * from dojos;

SELECT * FROM ninjas 
JOIN dojos ON dojos.id = ninjas.dojo_id;

insert into ninjas (first_name, last_name, age, dojo_id) values ('Adi', 'Chakra', 20, 100);
insert into ninjas (first_name, last_name, age, dojo_id) values ('Adrian', 'Dowst', 20, 100);
insert into ninjas (first_name, last_name, age, dojo_id) values ('Angel', 'Ruval', 20, 100);
insert into ninjas (first_name, last_name, age, dojo_id) values ('Adi', 'Chakra', 20, 101);
insert into ninjas (first_name, last_name, age, dojo_id) values ('Adrian', 'Dowst', 20, 101);
insert into ninjas (first_name, last_name, age, dojo_id) values ('Angel', 'Ruval', 20, 101);
insert into ninjas (first_name, last_name, age, dojo_id) values ('Adi', 'Chakra', 20, 102);
insert into ninjas (first_name, last_name, age, dojo_id) values ('Adrian', 'Dowst', 20, 102);
insert into ninjas (first_name, last_name, age, dojo_id) values ('Angel', 'Ruval', 20, 102);

select * from ninjas
JOIN dojos ON dojos.id = ninjas.dojo_id
where name = 'Dojo1';

select * from ninjas
JOIN dojos ON dojos.id = ninjas.dojo_id
where name = 'Dojo3';

select name from ninjas
JOIN dojos ON dojos.id = ninjas.dojo_id
where ninjas.id = 41;


