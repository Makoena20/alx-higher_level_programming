-- Create id_not_null table if it doesn't exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

-- Insert data into id_not_null table
INSERT INTO id_not_null (id, name) VALUES (1, "Holberton School");
INSERT INTO id_not_null (id, name) VALUES (1, "Python is cool");
INSERT INTO id_not_null (id, name) VALUES (2, "Holberton");
INSERT INTO id_not_null (id, name) VALUES (3, "School");
INSERT INTO id_not_null (id, name) VALUES (4, "C is fun");
INSERT INTO id_not_null (id, name) VALUES (89, "Best School");

