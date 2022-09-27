#!/usr/bin/python3
"""
write str to a text file and return number of characters added
"""


def write_file(filename="", text=""):
    """ function to write to text file
    Args:
        filename(str): name of textfile
        text(str): text to add
    Returns:
        number of chars(int)
    """
    with open(filename, mode = "w", encoding="utf-8") as new_file:
    new_file.write(text)
    return len(text)
