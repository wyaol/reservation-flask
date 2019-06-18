-- 创建teacher表
drop database if exists teacher;
create table teacher(
    id int not null primary key,
    password varchar(200) not null,
    name varchar(200) default null,
    sex varchar(200) default null,
    age smallint default null,
    college varchar(200) default null
);