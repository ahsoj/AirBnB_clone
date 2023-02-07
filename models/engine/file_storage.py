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

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return all nistances and objects"""
        return self.__objects

    def new(self, obj):
        """create new instance"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serialize data from dict object """
        with open(self.__file_path, 'w') as fp:
            dict_map = {}
            for k,v in self.__objects.items():
                dict_map[k] = v.to_dict()

            json.dump(dict_map, fp)

    def reload(self):
        """deserialize data from file"""
        try:
            with open(self.__file_path, 'r') as fp:
                for obj in json.load(fp).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return

