#!/usr/bin/python3
"""
"""
from datetime import datetime
import uuid


time = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """
    The BaseModel class to parent subclasses
    """
    def __init__(self):
        """Initialization for BaseModel"""
        uniq_id = uuid.uuid4()
        self.id = str(uniq_id)
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel"""
        return "[{:s}] ({:s}) {}".format(type(self).__name__,
                                         self.id,
                                         self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of self.__dict__"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        return new_dict
