drop database db;

create database db;

use db;

CREATE TABLE MyAppUsers(
	unique_id int primary key,
	firstName VARCHAR(15) NOT NULL,
    lastName VARCHAR(15) NOT NULL
    );
    
insert into myappusers values(2, 'ab', 'ag');
SELECT * FROM myappusers;
delete from myappusers where unique_id=3;


