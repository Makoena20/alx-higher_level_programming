#!/usr/bin/python3
"""
Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Construct the SQL query using user input
    sql = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    state_name = sys.argv[4]

    # Execute the SQL query
    cursor.execute(sql, (state_name,))

    # Fetch all the rows in a list of lists
    results = cursor.fetchall()

    # Display the results
    for row in results:
        print(row)

    # Disconnect from server
    cursor.close()
    db.close()

