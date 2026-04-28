what is the database?
database is a collection of structured data 

what is sql?
structured query language it help to communicate with database

why is sql?
its the bridge between data and human

DDL data defination language : ddl is the command where we can define the table/datbase 
create drop alter truncate
DML: data manipulation language: dml is a command where we can modify the data in table
delete update


constraints: constraints are the rules which are applying to column to ensure data accuracy and integrity. it ensure that data enter in database is valid and consistent.

keys in sql
unique key: column data should be unique. multiple column or set of columns can be unique 
primary key: data should be unique and not null. only one primary key in a table
forign key: data should be point to another table it help on joins

joins:joins are useful when we need to connect 2 tables means commiunicate
inner join
left join 
right join
outer join

views: its a virtual table on the result based sql query



----------------------------------------------------------------------------------------------------
<!-- create datbase -->
create database db
<!-- create table -->
create table tb (name varchar(250), id int)
<!-- insert command -->
insert into tb values ('harsh',25)
insert into tb (id) values (35)

<!-- alter command -->
alter table tb add column age int
alter table tb drop column id
alter table tb rename column age into id

<!-- drop command -->
drop table if exist tb
<!-- select command -->
select * from tb
<!-- limit command -->
select * from table tb limit 5
<!-- where condition -->
select * from table tb where id='35'
<!-- and /or -->
select * from table tb where id ='35' and name is null;
select * from table tb where id ='35' or name is not null

<!-- like -->
select * from tb where name like 'h%'
select * from tb where name like '%h'
select * from tb where name like '_a%'
select * from tb where name like '%s_'

<!-- sorting -->
select * from tb order by id asc or
select * from tb order by id 
select * from tb order by id desc

<!-- alias -->
select id as age from tb

<!-- grouping+having -->
select max(salary) from employee group by dept 
select avg(salary) from employee group by dept having avg(salary)>5000

<!-- joins -->
select a.*,b.* from table_a a inner join table_b b on a.id=b.id
select a.*,b.* from table_a a left join table_b b on a.id=b.id
select a.*,b.* from table_a a right join table_b b on a.id=b.id

<!-- union -->
select * from a
union 
select * from b

<!-- update -->
update table tb set id =40 where name is null

<!-- delete command -->
delete table tb where name is null

<!-- date transformation -->
select now() as date, year(date),month(date),date(date),dayname(date) from tb

<!-- type casting -->
select cast(id as varchar(200)) from tb

<!-- string fn -->
select upper(name),lower(name),concat(first_name,' ',last_name),concat_ws(first_name,last_name) from tb

<!-- conditions -->
select case when name is null then 'notavilable' else name end as cal_name from tb

<!-- window fn -->
select salary,name , dense_rank() over( salary order by desc) as rw from tb where rw=5
select salary,name , rank() over( salary order by desc) as rw from tb where rw=5
select salary,name , row_number() over( salary order by desc) as rw from tb where rw=5

select salary,name , dense_rank() over( partition by dept order by desc) as rw from tb where rw=5

<!-- subquery -->
select max(salary) from tb where salary< (select max(salary) from tb)

<!-- cte -->
with max_sal as (select max(salary) from tb)

select max(salary) from tb
left join max_sal on tb.id=max_sal.id where salary<max_sal.salary

<!-- views -->
create view v1 as (select * from tb)
