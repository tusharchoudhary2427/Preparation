-- A subquery is a query nested inside another query. Subqueries are useful for breaking down complex problems into smaller parts.

-- subquery using where -> 
select id, name, salary from users 
where salary > (select avg(salary) from users);

-- subquery using in -> find users who have been referred by someone who earns more than ₹50,000.
select id, name, referred_by_id from users
where referred_by_id in 
	(select id from users where salary > 50000);
    
