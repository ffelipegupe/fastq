#!/usr/bin/python3
""" BaseModel Class module """
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """ BaseModel that defines all common attributes/methods for other classes """
    def __init__(self, *args, **kwargs):
        """ Instantation """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            datefor = '%Y-%m-%dT%H:%M:%S.%f'
            self.id = kwargs.get('id')
            ca = datetime.strptime(kwargs.get('created_at'), datefor)
            self.created_at = ca
            ua = datetime.strptime(kwargs.get('updated_at'), datefor)
            self.updated_at = ua
        else:
            models.storage.new(self)

    def __str__(self):
        """ __str__ modification """
        a = type(self).__name__
        b = self.id
        c = self.__dict__
        return "[{}] ({}) {}".format(a, b, c)

    def save(self):
        """ Updates the public instance attribute updated_at
        with the current datetime """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance """
        ndict = self.__dict__.copy()
        ndict['__class__'] = self.__class__.__name__
        ndict['created_at'] = self.created_at.isoformat()
        ndict['updated_at'] = self.updated_at.isoformat()
        return ndict
