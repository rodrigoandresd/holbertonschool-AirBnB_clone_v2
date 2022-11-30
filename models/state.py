#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete, delete-orphan",
                          backref='state')

    @property
    def cities(self):
        """Return a list with the cities"""
        from models import storage
        city_dict = storage.all(City)
        city_list = []
        for value in city_dict.values():
            if value.state_id == self.id:
                city_list.append(value)
        return city_list
