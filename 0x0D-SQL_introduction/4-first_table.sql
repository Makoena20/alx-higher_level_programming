/*
Creates a table called first_table in the current database in MySQL server.
If the table first_table already exists, the script should not fail.
The database name will be passed as an argument of the mysql command.
If the table first_table exists, it will output 'Table exists before'.
If the table first_table does not exist, it will output 'Table doesn’t exist'.
*/

-- Check if the table exists
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);

-- Check if the table existed before
SELECT CASE
    WHEN EXISTS (
        SELECT 1
        FROM information_schema.tables
        WHERE table_schema = DATABASE()
        AND table_name = 'first_table'
    )
    THEN 'Table exists before'
    ELSE 'Table doesn’t exist'
END;

