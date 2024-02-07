#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel
from models.amenity import Amenity


class Amenity(BaseModel):
    """Represent an amenity"""

    name: str = ""
