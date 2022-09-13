#!/usr/bin/python3
"""A class that defines an object that must be
a specific type (int)"""


class Square:
    """a defined class"""
    def __init__(self, size=0, position=(0, 0)):
        """class intialization"""
        self.size = size
        """assign arg to class"""
        self.position = position

    @property
    def size(self):
        """getting field of object from intialized class"""
        return self.__size

    @size.setter
    def size(self, value):
        """setting conditions to control field data"""
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """getting field of object from intialized class"""
        return self.__position

    @position.setter
    def position(self, value):
        """setting conditions to control field data"""
        if type(value) is tuple and len(value) == 2 and \
            value[0] >= 0 and value[1] >= 0 and \
                type(value[0]) is int and type(value[1]) is int:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """getting method to return to public"""
        return (self.__size) ** 2

    def my_print(self):
        """print to standard output"""
        if (self.__size) == 0:
            print("")
            return
        else:
            for i in range(position[1]):
                print()
            for x in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
