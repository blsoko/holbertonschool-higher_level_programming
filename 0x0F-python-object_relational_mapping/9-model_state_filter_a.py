#!/usr/bin/python3
"""Write a script that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import desc

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(engine)
    session = Session()

    Base.metadata.create_all(engine)

    queryState = session.query(State).filter(
                State.name.contains('a')).order_by(State.id)
    for query in queryState:
        print("{}: {}".format(query.id, query.name))
