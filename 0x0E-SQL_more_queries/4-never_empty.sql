/*
 * Task: Create a script that creates the table id_not_null on the MySQL server.
 *       The table should have an 'id' column of type INT with a default value of 1,
 *       and a 'name' column of type VARCHAR(256).
 *       If the table id_not_null already exists, the script should not fail.
 */

-- Create table id_not_null if it doesn't exist
CREATE TABLE IF NOT EXISTS id_not_null (
    -- id column with default value 1
    id INT DEFAULT 1,
    -- name column
    name VARCHAR(256)
);

-- Insert values into the table id_not_null
-- Regular inserts
INSERT INTO id_not_null (id, name) VALUES (89, "Best School");

-- Insert values without specifying id
INSERT INTO id_not_null (name) VALUES ("Best");

