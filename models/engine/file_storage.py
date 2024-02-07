#!/usr/bin/python3
"""FileStorage model is defined here"""
import json
from models.base_model import BaseModel
from models import storage

class Filestorage:
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """Add a file to the FileStorage."""
        key = "{}.{}".format(obj.__class__.__name__, id(obj))
        self.__objects[key] = obj

    def save(self):
        """serialize"""
        serialized_object = {}
        for key, obj in self.__objects.items():
            serialized_object[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(serialized_object, file)

    def all(self):
        return self.__objects
    
    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it only exists."""
        try:
            with open(self.__file_path, "w") as file:
                serialized_object = json.load(file)
            for key, obj in self.__objects.items():
        except (FileNotFoundError) as fnf_error:
            print("No data file found, starting from scratch.")
            return self.__objects

