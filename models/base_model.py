#!/usr/bin/python3
"""basemodel is defined at this point"""

import uuid
from datetime import datetime

class BaseModel:
    """BaseModel for creating and managing files"""

    def __init__(self, *args, **kwargs):
        """initialize a new instance of BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary representation of BaseModel instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()  # Serialize datetime to ISO 8601 format
        obj_dict['updated_at'] = self.updated_at.isoformat()  # Serialize datetime to ISO 8601 format
        return obj_dict

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()
        from models import storage
        storage.new(self)
        storage.save()

    def __str__(self):
        """Return string representation of BaseModel instance"""
        class_name = self.__class__.__name__
        return "[{}] [{}] {}".format(class_name, self.id, self.__dict__)

if __name__ == "__main__":
    user = BaseModel()
    print(user.id)
    print(user.created_at)
    print(user.updated_at)

