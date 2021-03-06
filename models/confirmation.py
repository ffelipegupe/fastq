#!/usr/bin/python3
"""Confirmation class module"""

import models
from models.base import BaseModel, Base
#from models.store import Store
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Confirmation(BaseModel, Base):
    """ Order class body """
    if models.storage_t == "db":
        __tablename__ = 'confirmations'
        order_number = Column(Integer, nullable=False, default=0)
        store_id = Column(String(60), ForeignKey('stores.id'),nullable=False)
        order_id = Column(String(60), ForeignKey('orders.id'), nullable=False)
        status = Column(String(60), nullable=False)

    else:
        order_number = ""
        store_id = ""
        price = ""
        order_id = ""
        status = ""
        total = ""

    def __init__(self, *args, **kwargs):
        """initializes orders"""
        super().__init__(*args, **kwargs)
