/*
   Convert hbtn_0c_0 database to UTF8
*/

-- Connect to the MySQL server
-- Run the following SQL script to convert the database, table, and field to UTF8

-- Convert database to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert table to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert field to UTF8
ALTER TABLE first_table MODIFY COLUMN name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

