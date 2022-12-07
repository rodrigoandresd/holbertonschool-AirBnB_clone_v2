#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv

HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base if HBNB_TYPE_STORAGE == 'db' else object):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state', cascade="all, delete")
                          

    if HBNB_TYPE_STORAGE != "db":
        name = ''

        @property
        def cities(self):
            from models import storage
            return [city for city in list(storage.all(City).values())
                    if city.state_id == self.id]
