#!/usr/bin/python3
"""
contains the FileStorage class
"""
import json
from models.base_model import BaseModel


classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """
    Class that serializes instances to JSON and deserializes JSON
    file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all(self): returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """all(self): returns the dictionary __objects"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path) as f:
                json_obj = json.load(f)
            for key in json_obj.keys():
                self.__objects[key] = classes[
                                              json_obj[key]["__class__"]
                                             ](**json_obj[key])
        except FileNotFoundError:
            pass
