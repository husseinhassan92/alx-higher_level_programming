#!/usr/bin/python3
"""
return state id given state name; SQL injection free
parameters given to script: username, password, database, state name to match
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1],
                                   argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_s = State(name="California")
    new_c = City(name="San Francisco")
    new_s.cities.append(new_c)

    session.add(new_s)
    session.add(new_c)

    session.commit()
    session.close()
