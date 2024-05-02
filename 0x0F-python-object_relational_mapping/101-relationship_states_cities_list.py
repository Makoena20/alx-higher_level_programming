#!/usr/bin/python3
"""Module that lists all State objects and corresponding City objects in a database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

def list_states_cities(username, password, db_name):
    """Lists all State objects and corresponding City objects in the database"""

    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, db_name), pool_pre_ping=True)

    # Create session maker bound to engine
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Query to fetch all states and corresponding cities
    states = session.query(State).order_by(State.id).all()

    # Iterate over states and print corresponding cities
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        sys.exit(1)

    list_states_cities(sys.argv[1], sys.argv[2], sys.argv[3])

