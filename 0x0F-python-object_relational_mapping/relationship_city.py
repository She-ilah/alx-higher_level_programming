#!/usr/bin/python3
"""Contains the class definition of a City"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base

class City(Base):
    """Class representation of states table"""
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
