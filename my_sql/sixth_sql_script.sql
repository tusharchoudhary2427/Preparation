-- Transactions and AutoCommit 
-- every SQL statement is treated as a transaction and is committed automatically.

use startsql;

set autocommit = 0;
select * from users;
delete from users where id = 6;
rollback;
commit;
select * from users;
set autocommit = 1;

select * from users;