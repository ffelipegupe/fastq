#!/usr/bin/python3
"""Drink class module"""
import models
from models.base import BaseModel, Base
#from models.store import Store
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Drink(BaseModel, Base):
    """ Drink class body """
    if models.storage_t == "db":
        __tablename__ = 'drinks'
        name = Column(String(128), nullable=False)
        store_id = Column(String(60), ForeignKey('stores.id'), nullable=False)
        price = Column(Integer, nullable=False, default=0)
        inventory = Column(Integer, nullable=False, default=0)
    else:
        store_id = ""
        name = ""
        price = ""

    def __init__(self, *args, **kwargs):
        """initializes drinks"""
        super().__init__(*args, **kwargs)
