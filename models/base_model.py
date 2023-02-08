#!/usr/bin/python3
"""Create BaseModel for Defining \
        id: str/uuid \
        created_at: datetime \
        updated_at: datetime \
"""
import uuid
from datetime import datetime


class BaseModel:

    def __init__(self, *args, **kwargs):
        """
            *args:str/int
            **kwargs:dict
            if kwargs avail set attribute with setattr \
             methods else return current instance
        """
        from inits import storage
        if kwargs:
            for k,v in kwargs.items():
                if k != '__class__':
                    if k in ['created_at', 'updated_at']:
                        setattr(self, k, datetime.fromisoformat(v))
                    else:
                        setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """
            updates the public instance attribute \
            updated_at with the current datetime
        """

        from inits import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all \
            keys/values of __dict__ of the instance:
        """

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        for key,value in self.__dict__.items():
            if key in ["created_at", "updated_at"]:
                value = self.__dict__[key].isoformat()
                my_dict[key] = value
            my_dict[key] = value
        return my_dict

    def __str__(self):
        """return the hole information with\
            [<class name>] (<self.id>) <self.__dict__> \
            format \
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
