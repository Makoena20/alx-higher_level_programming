#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects
from the database hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Get the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the engine and session
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database and print the results
    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    # Close the session
    session.close()
