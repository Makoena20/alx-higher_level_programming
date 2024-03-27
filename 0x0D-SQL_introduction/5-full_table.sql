/*
 * This script prints the full description of the table first_table from the database hbtn_0c_0
 * without using the DESCRIBE or EXPLAIN statements.
 */

/* Retrieve table structure using INFORMATION_SCHEMA */

SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT, COLUMN_COMMENT
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'first_table';

