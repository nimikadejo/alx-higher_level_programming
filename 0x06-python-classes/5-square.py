#!/usr/bin/python3
"""A class that defines an object that must be
a specific type (int)"""


class Square:
    """a defined class"""
    def __init__(self, size=0):
        """class intialization"""
        self.size = size
        """assign arg to class"""

    @property
    def size(self):
        """getting field of object from intialized class"""
        return self.__size

    @size.setter
    def size(self, value):
        """setting conditions to control field data"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """getting method to return to public"""
        return (self.__size) ** 2

    def my_print(self):
        """printing to std output"""
        if (self.__size) == 0:
            print("")
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
