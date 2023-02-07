#!/usr/bin/python3
""" a class FileStorage that serializes instances to a \
    JSON file and deserializes JSON file to instances:"""
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        with open(self.__file_path, 'w') as fp:
            dict_map = {}
            for k,v in self.__objects.items():
                dict_map[k] = v.to_dict()

            json.dump(dict_map, fp)

    def reload(self):
        if self.__file_path:
            with open(self.__file_path, 'r') as fp:
                json.load(fp)

