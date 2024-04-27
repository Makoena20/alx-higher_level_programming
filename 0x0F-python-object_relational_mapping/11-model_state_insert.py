#!/usr/bin/python3
"""
Module: 11-model_state_insert.py
Adds the State object "Louisiana" to the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    """Main function"""
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create an engine to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Add Louisiana to the database
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the new state's id
    print(new_state.id)

if __name__ == "__main__":
    main()

