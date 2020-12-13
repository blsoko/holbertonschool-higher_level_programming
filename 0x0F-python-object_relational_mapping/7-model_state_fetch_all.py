#!/usr/bin/python3
"""Write a script that lists all State objects
from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format(sys.argv[1], sys.argv[2], sys.argv[3]))

Session = sessionmaker(engine)
session = Session()

if __name__ == '__main__':
    count = 0
    Base.metadata.create_all(engine)

    name = session.query(State).all()
    for names in name:
        count += 1
        print("{}: ".format(count), end='')
        print(names.name)
