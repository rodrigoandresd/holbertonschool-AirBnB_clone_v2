#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
from os import getenv

HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')


metadata = Base.metadata
place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base if HBNB_TYPE_STORAGE == 'db' else object):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship('Review', backref='place', cascade='all, delete')
    amenities = relationship('Amenity', secondary=place_amenity,
                             viewonly=False)

    if HBNB_TYPE_STORAGE != 'db':
        @property
        def reviews(self):
            """Return a list with the citites"""
            from models import storage
            review_dict = storage.all(Review)
            review_list = []
            for value in review_dict.values():
                if value.place_id == self.id:
                    review_list.append(value)
            return review_list

        @property
        def amenities(self):
            from models import storage
            amenity_dict = storage.all(Review)
            amenity_list = []
            for value in amenity_dict.values():
                if value.amenity.id == self.amenity_ids:
                    amenity_list.append(value)
            return amenity_list

        @amenities.setter
        def amenities(self, obj):
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
