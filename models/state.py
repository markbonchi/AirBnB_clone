#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel


class State(BaseModel):
    """Representation of Stast"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
