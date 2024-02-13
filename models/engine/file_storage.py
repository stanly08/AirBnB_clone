#!/usr/bin/python3
"""FileStorage model is defined here"""
import json
import os
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User
from datetime import datetime

class FileStorage:
    """Class for serializing and deserializing instances to and from JSON file."""

    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """Add a new object to the __objects dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        Filestorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON and save to file."""
        serialized_objects = {}
        for key, value in Filestorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(Filestorage.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserialize JSON file to __objects dictionary."""
        try:
            with open(Filestorage.__file_path, "r") as file:
                # Check if the file is empty
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    cls = eval(class_name)
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

    def all(self):
        return Filestorage.__objects

