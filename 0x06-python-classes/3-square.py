#!usr/bin/python3
"""A class that defines an object that must be
a specific type (int)"""


class Square:
    """a defined class"""
    def __init__(self, size=0):
        """class intialization"""
        if isdigit(size) is False:
            """loop to make sure size input is
            an integer"""
            raise TypeError("size must be an integer")
        """assigning error message for type err"""
        else:
            if size < 0:
                raise ValueError("size must be <= 0")
                """raising an exception for negative
                integers"""
            else:
                self.__size = size
                """assigning field to an object"""

    def area(self):
        """new object to return suare value of square"""
        return (self.__size)
        """returns value of init"""
