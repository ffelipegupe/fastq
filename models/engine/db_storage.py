#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.base import BaseModel, Base
from models.store import Store
from models.food import Food
from models.drink import Drink
from models.order import Order
from models.confirmation import Confirmation
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Store": Store,
           "Food": Food}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        FASTQ_MYSQL_USER = getenv('FASTQ_MYSQL_USER')
        FASTQ_MYSQL_PWD = getenv('FASTQ_MYSQL_PWD')
        FASTQ_MYSQL_HOST = getenv('FASTQ_MYSQL_HOST')
        FASTQ_MYSQL_DB = getenv('FASTQ_MYSQL_DB')
        FASTQ_ENV = getenv('FASTQ_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(FASTQ_MYSQL_USER,
                                             FASTQ_MYSQL_PWD,
                                             FASTQ_MYSQL_HOST,
                                             FASTQ_MYSQL_DB))
        #if HBNB_ENV == "test":
        #    Base.metadata.drop_all(self.__engine)

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
        """Method retrieves one object"""
        if cls is not None and id is not None:
            cls_objs = models.storage.all(cls)
            for value in cls_objs.values():
                if (value.id == id):
                    return value
            else:
                return None

    def count(self, cls=None):
        """method to count the number of objects in storage"""
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count
