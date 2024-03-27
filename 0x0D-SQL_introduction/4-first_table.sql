-- Create a table called first_table in the current database if it doesn't exist

-- Check if the table first_table already exists
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
