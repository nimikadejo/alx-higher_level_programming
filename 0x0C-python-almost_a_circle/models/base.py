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
        if self.id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
