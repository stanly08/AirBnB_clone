#!/usr/bin/python3
"""basemodel is defined at this point"""

import uuid
from datetime import datetime, date, time

class BaseModel:
    """BaseModel for creationg and managing files"""

    def __init__(self, *args, **kwargs):
        """initialize a new instance of BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformart()

    def __str__(self):
        class_name = self.__class__.__name__

        return "[{}] [{}] {}".format(class_name, self.id, self.__dict__)

user = BaseModel()

print(user.id)
print(user.created_at)
print(user.updated_at)

