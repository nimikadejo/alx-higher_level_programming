#!/usr/bin/python3
"""
contains to_json_string
"""
import json


def to_json_string(my_obj):
    """ functiom that returns JSON rep of a str obj
    Args:
        my_obj(str): object
    Returns:
        JSON rep of object
    """
    return json.dumps(my_obj)
