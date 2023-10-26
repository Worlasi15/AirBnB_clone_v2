#!/usr/bin/python3

"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
	    if cls is not None:
	    return {k: v for k, v in FileStorage.__objects.items()
		    if isinstance(v, cls)}
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
	    key = "{}.{}".format(obj.__class__.__name__, obj.id)
	    FileStorage.__objects[key] =  obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {k: v.to_dict() for k, v in FileStorage.__objects.items()}}
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel

	 try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    cls_name = val["__class__"]
                    self.all()[key] = BaseModel(**val)
		    except FileNotFoundError:
            pass

    def delete(self, obj=None):
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            del FileStorage.__objects[key]
