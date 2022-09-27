#!/usr/bin/python3
"""
Function that reads a text file and prints to std out
"""


def read_file(filename=""):
    """ function to read and print text file to std out
    Args:
    filename(str): name of text file 
    """
    with open(filename, encoding="utf-8") as f:
        read_content = f.read()
        print(read_content, end="")
