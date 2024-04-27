#!/usr/bin/python3
"""
Module for safe filtering of states from a MySQL database.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL database
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object
    cur = conn.cursor()

    # Execute the query
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC", (sys.argv[4],))

    # Fetch all the rows
    rows = cur.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close cursor
    cur.close()

    # Close connection
    conn.close()

