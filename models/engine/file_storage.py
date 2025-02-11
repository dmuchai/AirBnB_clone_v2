#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review
        }


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of objects"""
        if not cls:
            return self.__objects
        elif isinstance(cls, str):
            return {key: objects for key, objects in self.__objects.items()
                    if objects.__class__.__name__ == cls}
        else:
            return {key: objects for key, objects in self.__objects.items()
                    if isinstance(objects, cls)}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        json_obj = {
                key: obj.to_dict(save_to_disk=True)
                for key, obj in self.__objects.items()
        }
        with open(self.__file_path, 'w') as f:
            json.dump(json_obj, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.__objects[key] = classes[val['__class__']](**val)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside."""
        if obj:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def close(self):
        """Calls reload method for deserializing JSON file to objects."""
        self.reload()

    def get(self, cls, id):
        """Retrieves a single object by class and ID"""
        if (
            cls and isinstance(cls, str) and id and isinstance(id, str)
            and cls in classes
        ):
            return self.__objects.get(f"{cls}.{id}", None)
        return None

    def count(self, cls=None):
        """Counts the number of objects in storage"""
        return len(self.all(cls))
