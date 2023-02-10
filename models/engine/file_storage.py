#!/usr/bin/python3
"""File Storage Cls: Serializes and Deserializes instances to a JSON
"""
import json


class FileStorage:
    """
    Serialize and deserialize instances to and fron JSON
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary '__objects'
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Writes into __objetcs, key <obj class name>.id,
        with obj as the value
        """
        key = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to JSON file
        path: __file_path
        """
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(my_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects, if JSON file(__file_path) exists
        Otherwise, do nothing. if file does not exist, no exception is raised
        """
        from models.base_model import BaseModel

        class_dict = {"BaseModel":BaseModel}
        obj = {}
        try:
            with open(FileStorage.__file_path, "r") as f:
                json_obj = json.load(f)
                for key, value in json_obj.items():
                    obj[key] = class_dict[value["__class__"]](**value)
                FileStorage.__objects = obj
        except FileNotFoundError:
            pass
