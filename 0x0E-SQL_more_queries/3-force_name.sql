-- Create table force_name if it doesn't exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

-- Inserting data into force_name table
INSERT INTO force_name (id, name) VALUES (89, "Best School");

