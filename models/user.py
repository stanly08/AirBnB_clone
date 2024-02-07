#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel
from user import User

class User(BaseModel):
    """user representation"""

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
