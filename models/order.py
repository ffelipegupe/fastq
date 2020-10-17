#!/usr/bin/python3
"""Order class module"""

import models
from models.base import BaseModel, Base
from models.store import Store
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship

if models.storage_t == 'db':
    order_food = Table('order_food', Base.metadata,
                          Column('order_id', String(60),
                                 ForeignKey('orders.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('food_id', String(60),
                                 ForeignKey('foods.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))

    order_drink = Table('order_drink', Base.metadata,
                          Column('order_id', String(60),
                                 ForeignKey('orders.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('drink_id', String(60),
                                 ForeignKey('drinks.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))


class Order(BaseModel, Base):
    """ Order class body """
    if models.storage_t == "db":
        __tablename__ = 'orders'
        order_number = Column(String(128), nullable=False)
        store_id = Column(String(60), ForeignKey('stores.id'), nullable=False)
        price = Column(Integer, nullable=False, default=0)
        foods = relationship("Food", secondary=order_food,
                             viewonly=False)
        drinks = relationship("Drink", secondary=order_drink,
                              viewonly=False)
        units = Column(Integer, nullable=False, default=0)
        total = Column(Integer, nullable=False, default=0)
        user_name = Column(String(25), nullable=False)
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
