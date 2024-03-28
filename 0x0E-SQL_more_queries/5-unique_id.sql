-- Create or ensure existence of table unique_id with specified schema
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

-- Insertion of data into unique_id table
-- Correct output: unique_id doesn’t exist and regular inserts
-- Correct output: unique_id already exists, regular inserts and insert with id already inserted

INSERT INTO unique_id (id, name) VALUES (89, "Best School");
INSERT INTO unique_id (id, name) VALUES (89, "Best");

