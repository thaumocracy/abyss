create database jobs;
use jobs;
create table workers(
  id int not null auto_increment,
  primary key(id),
  first_name varchar(100) not null,
  last_name varchar(100) not null,
  middle_name varchar(100),
  age int not null,
  current_status varchar(100) not null default 'employed'
)