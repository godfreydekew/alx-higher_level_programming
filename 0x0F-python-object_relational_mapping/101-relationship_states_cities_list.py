#!/usr/bin/python3
"""lists all State objects, and corresponding
City objects, contained in the database hbtn_0e_101_usa"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    # Create a session for interacting with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State)
    for s in states:
        print(f"{s.id}: {s.name}")
        [print(f"    {c.id}: {c.name}") for c in s.cities]
