#!/usr/bin/python3
"""
contains from_json__string
"""
import json


def from_json_string(my_str):
    """ function that returns an object represented by a json string
    Args:
        my_str(str): string to convert
    Returns:
        object
    """
    return json.loads(my_str)
