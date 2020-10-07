#!/usr/bin/python3
"""Food class module"""

from models.base import BaseModel


class Food(BaseModel):
    """ Food class body """
    name = ""
    id = ""
    store_id = ""
    price = ""