use startersql;
-- Views -> A view in MySQL is a virtual table based on the result of a SELECT query. It does not store data itself — it always reflects the current data in the base tables.

create view high_salary_users as 
select name, salary
from users
where salary > 70000;

select * from high_salary_users;
update users set salary = 30000 where id = 2;
drop view high_salary_users;