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
    def to_json_string(list_dictionaries):
        """returns json of a dict"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string of list_objs to a file"""
        filename = cls.__name__ + ".json"
        list_copy = []
        if list_objs is not None:
            for i in list_objs:
                list_copy.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_copy))

    @staticmethod
    def from_json_string(json_string):
        """returns the list represented by the JSON string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all set attributes"""
        if cls.__name__ is "Rectangle":
            copy = cls(1, 1)
        elif cls.__name__ is "Square":
            copy = cls(1)
        copy.update(**dictionary)
        return copy

    @classmethod
    def load_from_file(cls):
        """ returns list of instances"""
        filename = cls.__name__ + ".json"
        list_ = []
        try:
            with open(filename, 'r') as f:
                list_ = cls.from_json_string(f.read())
            for i, e in enumerate(list_):
                list_[i] = cls.create(**list_[i])
        except Exception:
            pass
        return list_
