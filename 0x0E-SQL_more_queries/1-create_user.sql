-- Task: Create a MySQL server user user_0d_1 with all privileges and set the password to user_0d_1_pwd.
-- All SQL keywords should be in uppercase.

-- Create or update the user user_0d_1 with the password user_0d_1_pwd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to user_0d_1 on all databases
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;

