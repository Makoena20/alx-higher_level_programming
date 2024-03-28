/*
This script lists all privileges of the MySQL users user_0d_1 and user_0d_2 on the server.
*/

-- Check if user_0d_1 exists
SELECT USER, HOST FROM mysql.user WHERE USER = 'user_0d_1' AND HOST = 'localhost';

-- List privileges for user_0d_1 if exists
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Check if user_0d_2 exists
SELECT USER, HOST FROM mysql.user WHERE USER = 'user_0d_2' AND HOST = 'localhost';

-- List privileges for user_0d_2 if exists
SHOW GRANTS FOR 'user_0d_2'@'localhost';

