-- 创建teacher表
drop table if exists teacher;
create table teacher(
    wchat_id varchar(20) not null primary key,
    teacher_id varchar(20) not null,
    name varchar(200) default null,
    sex varchar(200) default null,
    age smallint default null,
    college varchar(200) default null,
    credit smallint default 0,
    pub_date timestamp null DEFAULT CURRENT_TIMESTAMP
);

-- 创建 task 表
drop table if exists task;
create table task(
    task_id int not null primary key AUTO_INCREMENT,
    teacher_id varchar(20) default null,
    finance_id varchar(20) default null,
    reservate_time timestamp null,
    actual_time timestamp null,
    status varchar(200) default '待完成'
);

-- 创建财务人员表
drop table if exists finance;
create table finance(
    wchat_id varchar(20) not null primary key,
    finance_id varchar(20) not null,
    name varchar(200) default null,
    sex varchar(200) default null,
    age smallint default null
);

-- 创建窗口表
drop table if exists window;
create table window(
    window_id varchar(20) not null primary key,
    finance_id varchar(20) null,
    status varchar(200) null
);