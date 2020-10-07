#!/usr/bin/python3
"""Confirmation class module"""

from models.base import BaseModel


class Confirmation(BaseModel):
    """ Confirmation class body """
    id = ""
    order_id = ""
    store_id = ""
    status = ""