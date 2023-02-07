#!/usr/bin/python3
""" a class FileStorage that serializes instances to a \
    JSON file and deserializes JSON file to instances:"""
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return dict(FileStorage.__objects)

    def new(self, obj):
        FileStorage.__objects['id'] = obj

    def save(self):
        if __file_path:
            with open(FileStorage.__file_path, 'w') as fp:
                json.dump(FileStorage.__objects, fp)

    def reload(self):
         with open(FileStorage.__file_path, 'r') as fp:
            json.load(fp)

