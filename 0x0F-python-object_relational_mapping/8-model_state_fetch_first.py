#!/usr/bin/python3

"""This module prints the first State object from the database hbtn_0e_6_usa"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    state = session.query(State).first()

    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")
