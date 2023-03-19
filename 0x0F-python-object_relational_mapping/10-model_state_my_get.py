#!/usr/bin/python3
"""
A ccript that prints the state object with the name
passed as argument from the database hbtn_0e_0_usa
"""

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter(
        State.name == argv[4]).order_by(State.id).all()
    if result:
        print(f"{result[0].id}")
    else:
        print("Not Found")
    session.close()
