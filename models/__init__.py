#!/usr/bin/python3
"""
 to create a unique FileStorage instance for your application
"""
from models.engine.file_storage import FileStoarge
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
    "User": User,
    "BaseModel": BaseModel,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review,
}

storage = FileStorage()
storage.reload()
