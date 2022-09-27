#!/usr/bin/python3
"""
contains save_to_json_file
"""


def save_to_json_file(my_obj, filename):
    """ function that writes an object to a text file using json
    Args:
        my_obj(any): object
        filename(str): textfile
    """
    with open(filename, mode="w", encoding="utf-8") as jf:
        jf.write(json.dumps(my_obj))
