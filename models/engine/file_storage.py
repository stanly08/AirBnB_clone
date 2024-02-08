"""FileStorage model is defined here"""
import json
import os
from models.base_model import BaseModel
from datetime import datetime

class FileStorage:
    """Class for serializing and deserializing instances to and from JSON file."""

    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """Add a new object to the __objects dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON and save to file."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserialize JSON file to __objects dictionary."""
        try:
            with open(self.__file_path, "r") as file:
                # Check if the file is empty
                if os.path.getsize(self.__file_path) == 0:
                    return
                serialized_objects = json.load(file)
                # Check if the loaded data is a dictionary
                if not isinstance(serialized_objects, dict):
                    return
                for key, value in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    value['created_at'] = datetime.strptime(value['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                    value['updated_at'] = datetime.strptime(value['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
                    self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass

    def all(self):
        """Return the dictionary of all objects."""
        return self.__objects

