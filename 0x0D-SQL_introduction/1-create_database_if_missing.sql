-- Script to create the database hbtn_0c_0 if it does not already exist

-- Check if the database hbtn_0c_0 exists
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;

-- Output message if the database did not exist before
SELECT 'Correct output: no database before' AS OutputMessage WHERE ROW_COUNT() = 1;

-- Output message if the database already exists
SELECT 'Correct output: with database already exists' AS OutputMessage WHERE ROW_COUNT() = 0;
