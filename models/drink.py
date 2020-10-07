#!/usr/bin/python3
"""Drink class module"""

from models.base import BaseModel


class Drink(BaseModel):
    """ Drink class body """
    name = ""
    id = ""
    store_id = ""
    price = ""