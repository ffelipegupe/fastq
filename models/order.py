#!/usr/bin/python3
"""Order class module"""

from models.base import BaseModel


class Order(BaseModel):
    """ Order class body """
    name = ""
    id = ""
    client_id = ""
    store_id = ""
    food_id = ""
    drink_id = ""
    menu_url = ""
    units = ""
    total = ""