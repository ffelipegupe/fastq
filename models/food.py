#!/usr/bin/python3
"""Food class module"""
import models
from models.base import BaseModel, Base
#from models.store import Store
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Food(BaseModel, Base):
    """ Food class body """
    if models.storage_t == "db":
        __tablename__ = 'foods'
        name = Column(String(128), nullable=False)
        store_id = Column(String(60), ForeignKey('stores.id'),nullable=False)
        price = Column(Integer, nullable=False, default=0)
        inventory = Column(Integer, nullable=False, default=0)
    else:
        store_id = ""
        name = ""
        price = ""

    def __init__(self, *args, **kwargs):
        """initializes food"""
        super().__init__(*args, **kwargs)
