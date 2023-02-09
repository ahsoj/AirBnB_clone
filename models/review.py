#!/usr/bin/python3
""" initialization ` Review ` class """
from models.base_model import BaseModel


class Review(BaseModel):
    """
        place_id: str
        user_id: str
        text: str
    """
    place_id = ""
    user_id = ""
    text = ""

