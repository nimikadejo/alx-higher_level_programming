#!/usr/bin/python3
"""
contains function append_write
"""


def append_write(filename="", text=""):
    """function to append a str at end of text file and return char length
    Args:
        filename(str): textfile
        text(str): text to append
    Returns:
        number of character added
    """
    with open(filename, mode="a", encoding="utf-8") as af:
        af.append(text)
    return len(text)
