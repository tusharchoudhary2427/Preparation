-- JOINs are used to combine rows from two or more tables based on related columns — usually a foreign key in one table referencing a primary key in another.

select * from users;
select * from addresses;
-- 1. INNER JOIN-> Returns only the matching rows from both tables.

 select users.name, gender, addresses.city, addresses.state, addresses.user_id as addresses_userid
 from users
 inner join addresses on users.id = addresses.user_id;

-- 2. LEFT JOIN -> Returns all rows from the left table (users), and matching rows from the right table (addresses). If no match is found, NULLs are returned.

 select users.name, gender, addresses.city, addresses.state, addresses.user_id as addresses_userid
 from users
 left join addresses on users.id = addresses.user_id;

-- 3. RIGHT JOIN -> Returns all rows from the right table (addresses), and matching rows from the left table (users). If no match is found, NULLs are returned.

select users.name, gender, addresses.city, addresses.state, addresses.user_id as addresses_userid
 from users
 right join addresses on users.id = addresses.user_id;
 
-- UNION and UNION ALL -> The UNION operator in SQL is used to combine the result sets of two or more SELECT statements. It removes duplicates by default.



