#!/usr/bin/python3
"""Write a script that prints the first
State object from the database hbtn_0e_6_usa"""

if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import desc

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(engine)
    session = Session()

    Base.metadata.create_all(engine)

    queryState = session.query(State).filter(State.id == 1)
    for names in queryState:
        if queryState:
            print("{}: {}".format(names.id, names.name))
        else:
            print("Nothing")
            break
