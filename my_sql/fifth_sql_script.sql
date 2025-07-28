-- Functions -> These helps you analyze, transform, or summarize data in your tables.

use startsql;

select * from users;

-- select count(*) from users;
-- select count(*) from users where gender = 'Male';
-- select  min(salary) as min_salary, max(salary) as max_salary from users;
-- select sum(salary) as total_payment from users;
-- select gender, avg(salary) as avg_salary from users group by gender;
-- select name, length(name) as name_length from users;
-- SELECT name, LOWER(name) AS lowercase_name FROM users;
-- SELECT name, UPPER(name) AS uppercase_name FROM users;
-- select name, concat(lower(name) , "8888") as username, now() as time from users;
-- select name, datediff(curdate(), date_of_birth) as dayslived from users;

-- SELECT salary,
--        ROUND(salary) AS rounded,
--        FLOOR(salary) AS floored,
--        CEIL(salary) AS ceiled
-- FROM users;

-- select name, gender,
-- 	   if(gender = 'Male', 'Yes', 'No') as is_male
--        from users;

