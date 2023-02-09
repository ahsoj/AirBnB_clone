#!/usr/bin/python3
""" initialization ``User class \
    for store user information 
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
        email: str
        password: str
        first_name: str
        last_name: str
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
