#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel
from models.review import Review



class Review(BaseModel):
    """Represent a review"""

    place_id: str = ""
    user_id: str = ""
    text: str = ""
