#!/usr/bin/python3
"""contains load_from_json_file"""
import json


def load_from_json_file(filename):
    """function to create object from a json file"""
    with open(filename, encoding="utf-8") as oj:
        return json.load(oj)
