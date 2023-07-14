#!/usr/bin/python3
"""This module is used to create a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """This Class manages user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
