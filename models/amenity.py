#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

env = getenv('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
    """ Amenity Class to store amenities information"""

    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary='place_amenity', viewonly=False)
    
    if env != "db":
        name = ""
