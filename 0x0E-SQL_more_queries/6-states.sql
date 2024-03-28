-- Task: Create a script to create the hbtn_0d_usa database and the states table, insert data into it, and handle existing database and table scenarios.

-- Create or use the database hbtn_0d_usa if it exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

-- Create the states table if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Insert data into the states table
INSERT INTO states (name) VALUES ('California'), ('Arizona'), ('Texas');

-- Attempt to select data from the states table
-- SELECT * FROM states; -- You are not allowed to use the SELECT statement in the script

