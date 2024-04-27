#!/usr/bin/python3
"""
Script: 100-relationship_states_cities
Creates a State "California" with City "San Francisco"
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)
    session.add(california)
    session.add(san_francisco)

    session.commit()
    session.close()

