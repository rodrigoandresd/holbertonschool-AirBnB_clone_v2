#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')


class User(BaseModel, Base if HBNB_TYPE_STORAGE == 'db' else object):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship('Place', backref='user', cascade='all, delete')
    reviews = relationship('Review', backref='user', cascade='all, delete')

    if HBNB_TYPE_STORAGE != "db":
        email = ''
        password = ''
        first_name = ''
        last_name = ''
