#!/usr/bin/python3
"""Script that lists all states with a name starting with N from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    # Fetch all rows using fetchall() method
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close the cursor
    cursor.close()

    # Close the database connection
    db.close()

