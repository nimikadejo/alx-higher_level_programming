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
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = self.__height = value
        self.__size = value

    def __str__(self):
        """ string rep of instantiation """
        return ("[Square] ({}) {}/{} - {}".format
                (self.__id, self.__x, self.__y, self.__size))
