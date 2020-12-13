#!/usr/bin/python3
"""Next, write a script 14-model_city_fetch_by_state.py
that prints all City objects from the database hbtn_0e_14_usa"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import desc
from model_city import City

if __name__ == '__main__':
    key = 0
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(engine)
    session = Session()

    Base.metadata.create_all(engine)
    objs = session.query(City, State).filter(City.state_id == State.id).all()
    for city, state in objs:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
