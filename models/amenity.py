#!/usr/bin/python
""" holds class Amenity"""
import models
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Representation of Amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes amenity"""
        super().__init__(*args, **kwargs)
