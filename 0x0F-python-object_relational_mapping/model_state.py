#!/usr/bin/python3
'''
Create State class and an instance Base = declarative_base(). Creates a
link to the database
'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    '''
    Saste class extending Base =>declarative base
    '''
    __tablename__ = 'states'
    id = Column(
        Integer, primary_key=True, nullable=False,
        unique=True, autoincrement=True
    )
    name = Column(String(128), nullable=False)
