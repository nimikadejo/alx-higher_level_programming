#!/usr/bin/python3
"""
module for retangle class
"""


from models.base import Base


class Rectangle(Base):
    """class defintion"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        __init__ - class initialization
        Args:
            width(int): width of class
            height(int): height of rectangle(class)
            x(int): variable of class
            y(int): variable ofclass
        Returns:
            None
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ width setter"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def id(self):
        """ id getter"""
        return self.__id

    @id.setter
    def id(self, id):
        """ id setter"""
        self.__id = id
