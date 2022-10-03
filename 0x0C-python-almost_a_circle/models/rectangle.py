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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            """ width getter """
            return self.__width

        @width.setter
        def width(self, value):
            """ width setter"""
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """ height getter """
            return self.__height

        @height.setter
        def height(self, value):
            """ height setter"""
            if type(value) != int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """x getter """
            return self.__x

        @x.setter
        def x(self, value):
            """ x setter"""
            if type(value) != int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            """y getter """
            return self.__y

        @y.setter
        def y(self, value):
            """ y setter"""
            if type(value) != int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
