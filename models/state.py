#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel
from state import State

class State(BaseModel):
    """Represent a state"""

    name: str = ""