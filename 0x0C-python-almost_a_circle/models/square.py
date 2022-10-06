#!/usr/bin/python3
""" module for class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ class definition"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        function to instantiate square class
        Args:
            size(int): size of square
            x(int): position of ''
            y(int): position of ''
            id(id): id of class square
        Returns:
            None
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        value = self.__width = self.__height
        self.__size = value
