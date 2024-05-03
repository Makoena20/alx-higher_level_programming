-- This script creates the table id_not_null if it doesn't already exist,
-- with id set as INT with default value 1 and name as VARCHAR(256).
-- It ensures that the id column is not nullable.

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);

