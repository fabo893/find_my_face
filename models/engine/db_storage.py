#!/usr/bin/python3
"""
    Class DBStorage
"""

import models
from models.base_model import BaseModel, Base
from models.known import Known
from models.unknown import Unknown
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


classes = {"Known": Known, "Unknown": Unknown}


class DBStorage:
    """ interacts with the MySQL database """
    __engine = None
    __session = None

    def __init__(self):
        """ To create the instance """
        FMF_USER = getenv('FMF_USER')
        self.__engine = create_engine('mysql+mysqlconnector://face_user:face_Pwd1@localhost/find_my_face')


    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """A method to retrieve one object"""
        obj_dict = self.all(cls)
        for key in obj_dict.values():
            if key.id == id:
                return key
        return None

    def count(self, cls=None):
        """A method to count the number of objects in storage"""
        if cls:
            return len(self.all(cls))
        return len(self.all())
