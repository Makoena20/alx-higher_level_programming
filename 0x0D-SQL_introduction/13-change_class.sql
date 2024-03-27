/*
Script: 13-change_class.sql

This script removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0.

Requirements:
- All SQL keywords should be in uppercase
- All SQL queries should have a comment just before
- All files should start by a comment describing the task
- All files should end with a new line
*/

-- Delete records with score <= 5
DELETE FROM second_table WHERE score <= 5;


