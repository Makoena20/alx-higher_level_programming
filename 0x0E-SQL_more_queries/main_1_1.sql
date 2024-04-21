-- Check if id_not_null exists
SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'id_not_null';

-- Insert rows into id_not_null table
INSERT INTO id_not_null (id, name) VALUES (1, 'Holberton School');
INSERT INTO id_not_null (id, name) VALUES (1, 'Python is cool');
INSERT INTO id_not_null (id, name) VALUES (1, 'School');
INSERT INTO id_not_null (id, name) VALUES (2, 'Holberton');
INSERT INTO id_not_null (id, name) VALUES (3, 'School');
INSERT INTO id_not_null (id, name) VALUES (4, 'C is fun');

