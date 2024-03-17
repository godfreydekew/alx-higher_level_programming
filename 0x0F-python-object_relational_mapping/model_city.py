#!/usr/bin/python3
""" create a table city using sqlAlchemy"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """
        Defines City class
        __tablename__(str): name of the table
        id(int): Primary key of the table
        name(str): city name
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
