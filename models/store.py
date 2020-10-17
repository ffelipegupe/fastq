#!/usr/bin/python3
"""Store class module"""
import models
from models.base import BaseModel, Base
from models.food import Food
from models.drink import Drink
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Store(BaseModel, Base):
    """ Store class body """
    if models.storage_t == "db":
        __tablename__ = 'stores'
        name = Column(String(128), nullable=False)
        menu_url = ""
        foods = relationship("Food", backref="store",
                             cascade="all, delete, delete-orphan")
        #drinks = relationship("Drink", backref="store")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes store"""
        super().__init__(*args, **kwargs)

    @property
    def foods(self):
        """getter for list of foods instances related to the store"""
        food_list = []
        all_foods = models.storage.all(Food)
        for food in all_foods.values():
            if food.store_id == self.id:
                food_list.append(food)
        return food_list

    @property
    def drinks(self):
        """getter for list of drinks instances related to the store"""
        drink_list = []
        all_drinks = models.storage.all(Drink)
        for drink in all_drinks.values():
            if drink.store_id == self.id:
                drink_list.append(drink)
        return drink_list
