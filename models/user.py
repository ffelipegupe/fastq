#!/usr/bin/python3
"""User class module"""

from models.base import BaseModel


class User(BaseModel):
    """ Store class body """
    name = ""
    id = ""
    phone = ""
    order_id = ""