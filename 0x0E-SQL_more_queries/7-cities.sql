-- Task: Create a script to create the database hbtn_0d_usa and the table cities in the database if they do not exist already. 
--       The table cities should have specific attributes as described.

-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the database
USE hbtn_0d_usa;

-- Create table cities if not exists
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

-- Insert data into cities table
INSERT INTO cities (state_id, name) VALUES (1, 'San Francisco');
INSERT INTO cities (state_id, name) VALUES (10, 'Paris');

