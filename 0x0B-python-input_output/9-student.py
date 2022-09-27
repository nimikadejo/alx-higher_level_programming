!/usr/bin/python3
""" contains Student Class"""


class Student:
    """Class definiton: Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ method that retrieves a dictionary representation of a class instance ie an object"""
        return self.__dict__
