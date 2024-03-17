#!/usr/bin/python3
""" create a table states using sqlAlchemy"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
        Defines State class
        __tablename__(str): name of the table
        id(int): Primary key of the table
        name(str): state name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
