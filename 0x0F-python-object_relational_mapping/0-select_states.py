#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])
        cursor = db.cursor()
        # Query to select all states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        # Fetch all results
        results = cursor.fetchall()
        # Print results
        for row in results:
            print(row)
        # Close cursor and database connection
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)

