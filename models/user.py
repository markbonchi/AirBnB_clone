#!/usr/bin/python3
"""Contains the User class"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """User class inheriting from BaseModel class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializez User"""
        super().__init__(*args, **kwargs)
