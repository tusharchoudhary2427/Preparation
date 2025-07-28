-- Indexes in MySQL are used to speed up data retrieval. They work like the index of a book — helping the database engine find rows faster, especially for searches, filters, and joins.

use startersql;
show indexes from users;
create index idx_email on users(email);
drop index idx_email on users;