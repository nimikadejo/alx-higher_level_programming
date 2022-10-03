#!/usr/bin/python3
"""this module contains base.py which implements the base class in this project
"""
import json
import turtle


class Base:
    """ class definition"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries: dict):
        """returns json of a"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
