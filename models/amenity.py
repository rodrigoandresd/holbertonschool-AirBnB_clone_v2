#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base if HBNB_TYPE_STORAGE == 'db' else object):
    """ Amenity Class to store amenities information"""

    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    
    if HBNB_TYPE_STORAGE != "db":
        name = ""
