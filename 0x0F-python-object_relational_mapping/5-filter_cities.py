#!/usr/bin/python3
"""
This script retrieves and lists all cities of a given state from the database.
"""

import MySQLdb
import sys

def filter_cities(username, password, db_name, state_name):
    """
    Retrieve and list all cities of a given state from the database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.
        state_name (str): Name of the state to filter cities.

    Returns:
        None
    """
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)

    # Create a cursor object
    cursor = db.cursor()

    # Prepare SQL query to retrieve cities of the given state
    sql_query = """SELECT cities.name FROM cities
                   JOIN states ON cities.state_id = states.id
                   WHERE states.name = %s
                   ORDER BY cities.id"""

    try:
        # Execute the SQL query
        cursor.execute(sql_query, (state_name,))

        # Fetch all the rows in a list of lists
        cities = cursor.fetchall()

        # Print the cities separated by commas
        print(", ".join(city[0] for city in cities))
    except Exception as e:
        print("Error:", e)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database_name> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name, state_name = sys.argv[1:]

    filter_cities(username, password, db_name, state_name)

