#!/usr/bin/python3
"""Script that prints the State object with the name passed as argument
   from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    """Main function to retrieve state by name"""
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_name".format(sys.argv[0]))
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve state by name
    state = session.query(State).filter(State.name == state_name).first()

    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()

if __name__ == "__main__":
    main()

