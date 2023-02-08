#!/usr/bin/python3
""" a class FileStorage that serializes instances to a \
    JSON file and deserializes JSON file to instances:"""
import json


class FileStorage:
    """
        private_instance attribute \
        for serialize and deserialize \
        data
    """
    __file_path = "model.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj: dict):
        """ create new intance of object """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        value = obj
        FileStorage.__objects[key] = value # .update({key: value})

    def save(self):
        """ save a current or new object of model """
        with open(FileStorage.__file_path, 'w') as fp:
            dict_obj = {}
            for k,v in FileStorage.__objects.items():
                dict_obj[k] = v.to_dict()
            json.dump(dict_obj, fp)

    def reload(self):
        """ reload file when it call for new """
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as fp:
                FileStorage.__objects = json.load(fp)
            for k,v in FileStorage.__objects.items():
                FileStorage.__objects[k] = v
                #FileStorage.__objects[k] = cls_(**v)
                #print(FileStorage.__objects)
        except FileNotFoundError:
            return

