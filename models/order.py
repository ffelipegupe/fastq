#!/usr/bin/python3
"""Order class module"""

import models
from models.base import BaseModel, Base
#from models.store import Store
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Order(BaseModel, Base):
    """ Order class body """
    if models.storage_t == "db":
        __tablename__ = 'orders'
        order_number = Column(String(128), nullable=False)
        #store_id = Column(String(60), ForeignKey('stores.id'),nullable=False)
        price = Column(Integer, nullable=False, default=0)
        food_id = ""
        drink_id = ""
        units = Column(Integer, nullable=False, default=0)
        total = Column(Integer, nullable=False, default=0)
        user_name = ""
        phone = Column(Integer, nullable=False, default=0)
    else:
        order_number = ""
        store_id = ""
        price = ""
        food_id = ""
        drink_id = ""
        units = ""
        total = ""
        user_name = ""
        phone = ""

    def __init__(self, *args, **kwargs):
        """initializes orders"""
        super().__init__(*args, **kwargs)
