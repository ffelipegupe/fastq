#!/usr/bin/python3
"""Store class module"""

from models.base import BaseModel


class Store(BaseModel):
    """ Store class body """
    name = ""
    id = ""
    client_id = ""
    menu_url = ""