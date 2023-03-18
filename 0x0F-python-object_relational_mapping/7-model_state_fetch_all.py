#!/usr/bin/python3
'''
Creates a link class to table in database
A script that lists all State objects from the database hbtn_0e_6_usa
'''

import MySQLdb
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":

    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)

    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)

    session = Session()

    for instance in session.query(State).order_by(State.id).all():
        print("{}: {}".format(instance.id, instance.name))

    session.close()
