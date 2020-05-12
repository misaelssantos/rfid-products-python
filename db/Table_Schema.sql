drop table if exists products;

create table products (
    tag text, 
    value integer
);

insert into products (tag, value) values ('pao', 1);
insert into products (tag, value) values ('leite', 1);
insert into products (tag, value) values ('ovo', 1);