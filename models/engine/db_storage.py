#!/usr/bin/python3
"""
    This module defines a class to manage storage of hbnb models using
    SQL Alchemy
"""
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class DBStorage:
    """ manage storage of hbnb models using SQL Alchemy """
    __engine = None
    __session = None
    all_classes = ["State", "City", "User", "Place", "Review"]

    def __init__(self):
        """Create the engine (self.__engine)"""

        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db),
            pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all()

    def all(self, cls=None):
        """
            Query on the current database session all objects depending
            of the class name
        """

        dict_new = {}
        if cls is None:
            for c in self.all_classes:
                c = eval(c)
                for instance in self.__session.query(c).all():
                    key = instance.__class__.__name__ + '.' + instance.id
                    dict_new[key] = instance
        else:
            for instance in self.__session.query(cls).all():
                key = instance.__class__.__name__+'.' + instance.id
                dict_new[key] = instance

        return dict_new

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database
        and create the current database session by by using a sessionmaker """

        Base.metadata.create_all(self.__engine)

        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))

        self.__session = Session()

    def close(self):
        self.__session.close()
