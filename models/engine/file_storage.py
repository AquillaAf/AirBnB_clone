#!/usr/bin/python3
import os
import json
class FileStorage:
    """this is the class that stores data(objects)"""
    
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return (self.__objects.copy())

    def new(self, obj):
        self.obj = obj
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj    
    
    def save(self):
        my_dict = {}

        with open(self.__file_path, "w", encoding="utf-8") as f:
            for key, obj in self.__objects.items():
                    self.__objects[key] = self.obj.to_dict()
            json.dump(self.__objects, f, indent=4)
    
    def reload(self):
        try:
            with open(self.__file_path, "r",encoding="utf-8") as f:
                try:
                    self.__objects = json.load(f)
                except json.JSONDecodeError:
                    self.__objects = {}
        except FileNotFoundError:
            pass
        
    """
    def reload(self):
            if not os.path.isfile(self.__file_path):
                    return
            with open(self.__file_path, "r", encoding="utf-8") as f:
                try:
                    obj_dict = json.load(f.readline())
                    obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            # TODO: should this overwrite or insert?
                    self.__objects = obj_dict
                except json.JSONDecodeError:
                    pass
                """
