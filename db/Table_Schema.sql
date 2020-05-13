drop table if exists products;

create table products (
    tag text, 
    name text,
    icon text,
    value integer
);

insert into products (tag, name, value) values ('pao', 'Pão', 1);
insert into products (tag, name, value) values ('leite', 'Leite', 1);
insert into products (tag, name, value) values ('ovo', 'Ovos', 1);
insert into products (tag, name, value) values ('biscoito', 'Biscoito', 1);
insert into products (tag, name, value) values ('achocolatado', 'Achocolatado', 1);