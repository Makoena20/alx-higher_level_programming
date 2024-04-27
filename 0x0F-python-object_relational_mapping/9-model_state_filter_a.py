#!/usr/bin/python3
"""
Module for listing all State objects that contain the letter a
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """
    Main function to list all State objects containing the letter a
    """
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        return

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query to fetch states containing the letter 'a', sorted by id
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    main()

