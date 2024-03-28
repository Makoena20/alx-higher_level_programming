-- Task: Create a script to create the database hbtn_0d_2 and the user user_0d_2 with appropriate privileges.

-- Create or use database hbtn_0d_2 if it already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Check if user_0d_2 already exists
SELECT COUNT(*)
FROM mysql.user
WHERE User = 'user_0d_2' AND Host = 'localhost';

-- If user_0d_2 doesn't exist, create the user with password and privileges
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant privileges to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Check if user_0d_2 exists
SELECT IF(EXISTS(SELECT 1 FROM mysql.user WHERE User = 'user_0d_2' AND Host = 'localhost'), 'user_0d_2 exists', 'user_0d_2 doesn’t exist');

-- Provide instructions to log in with user_0d_2
-- Correct output: try to login with user_0d_2

