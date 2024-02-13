#!/usr/bin/python3
"""FileStorage model is defined here"""
import json
import cmd
import os
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User  # Import the User class
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
                    if class_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
                    elif class_name == "Place":
                        self.__objects[key] = Place(**value)
                    elif class_name == "State":
                        self.__objects[key] = State(**value)
                    elif class_name == "City":
                        self.__objects[key] = City(**value)
                    elif class_name == "Amenity":
                        self.__objects[key] = Amenity(**value)
                    elif class_name == "Review":
                        self.__objects[key] = Review(**value)
                    elif class_name == "User":
                        self.__objects[key] = User(**value)
        except FileNotFoundError:
            pass

    def all(self, cls=None):
        """
        Returns a dictionary of all objects filtered by class name if provided.
        If no class name is provided, returns all objects.
        """
        if cls is None:
            return self.__objects

        filtered_objects = {}
        for key, obj in self.__objects.items():
            if key.split('.')[0] == cls.__name__:
                filtered_objects[key] = obj
        return filtered_objects

     def do_update(self, line):

        args = line.split()
        if len(args) == 0:
            print("class name missing")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User", "State", "City", "Place","Review", "Amenity"]:
            print("class doesn't exist")
            return
        if len(args) < 2:
            print("instance id missing")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all()
        if key not in all_objs:
            print("no instance found")
            return
        if len(args) < 3:
            print("attribute name missing")
            return
        attribute = args[2]
        if len(args) < 4:
            print("value missing")
            return
        value = args[3]
        try:
            value = eval(value)
        except:
            pass
        obj = all_objs[key]
        setattr(obj, attribute, value)
        obj.save()

