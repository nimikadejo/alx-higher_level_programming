#!/usr/bin/python3
"""contains class_to_json"""


def class_to_json(obj):
    """ returns dictionary description of an object
    that has been serialized with json"""
    return obj.__dict__
