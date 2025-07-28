-- A Self JOIN is a regular join, but the table is joined with itself.

use startersql;

alter table users
add column referred_by_id int after salary;

UPDATE users SET referred_by_id = 1 WHERE id IN (2, 3, 13, 15, 16, 18, 19); -- User 1 referred Users 2 and 3
UPDATE users SET referred_by_id = 2 WHERE id = 4;       -- User 2 referred User 4
select 
a.id,
a.name as user_name,
b.name as referred_by_name
from users a 
inner join users b on a.referred_by_id = b.id; 

select * from users;



