#!/usr/bin/python3
"""
contains the FileStorage class
"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """
    Class that serializes instances to JSON and deserializes JSON
    file to instances
    """

    __file_path = "file.json"
    __objects: dict = {}

    def all(self):
        """all(self): returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        with open(FileStorage.__file_path, "w") as f:
            json_dict = {k: v.to_dict() for k, v in odict.items()}
            f.write(json.dumps(json_dict))

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                json_obj = json.loads(f.read())
                for k, v in json_obj.items():
                    FileStorage.__objects[k] = classes[
                                                    v["__class__"]
                                                    ](**v)
        except FileNotFoundError:
            pass
