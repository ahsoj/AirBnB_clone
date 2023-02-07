#!/usr/bin/python3
"""class BaseModel that defines all common \
        attributes/methods for other classes"""
import uuid
import datetime
from models import storage


class BaseModel:
    """Initialize class of instances"""

    def __init__(self, *args, **kwargs):
        """
            *args:str/int
            **kwargs:dict
            if kwargs avail set attribute with setattr \
             methods else return current instance
        """
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k in ["created_at", "updated_at"]:
                        setattr(self, k, datetime.datetime.fromisoformat(v))
                    else:
                        setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.create_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def save(self):
        """
            updates the public instance attribute \
            updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all \
            keys/values of __dict__ of the instance:
        """
        my_dict = {}
        my_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key in ["created_at", "upadted_at"]:
                value = self.__dict__[key].isoformat()
                my_dict[key] = value
            my_dict[key] = value
        # my_dict["__class__"] = self.__class__.__name__
        return my_dict

    def __str__(self):
        """return the hole information with\
            [<class name>] (<self.id>) <self.__dict__> \
            format \
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
