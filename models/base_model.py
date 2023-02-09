#!/usr/bin/python3
"""Base Model Class Structure
"""
import uuid
from datetime import datetime

class BaseModel:
    """
    Class that defines all common attributes/methods
    for other classes.
    Public Attributes:
    id(string) - assign with an uuid when an instance is created
    created_at(datetime) - assign with a current datetime when instance is created
    updated_at(datetime) - assign with current datetime when an instance is created
    will be updated every time object is changed.
    Methods:
    __str__: to print [<class name>] (<self,id>) <self.__dict__>
    save(self): update public instance attribute updated_at with current datetime
    to_dict(self): return a dictionary containing all k/v of __dict__ of the instance
    """
    def __init__(self):

        """
        Class initialization with pblic methods
        as stated.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Return string representation as described
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update 'updated_at attribute' with current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dict containing all k/v of __dict__ of the instance
        """
        att_dict = self.__dict__.copy()
        att_dict["__class__"] = self.__class__.__name__
        att_dict["created_at"] = self.created_at.isoformat()
        att_dict["updated_at"] = self.updated_at.isoformat()
        return att_dict
