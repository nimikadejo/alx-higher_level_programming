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
            return self.width

        @width.setter
        def width(self, width):
            """ width setter"""

        @property
        def height(self):
            return self.height

        @height.setter
        def height(self, height):
            """ height setter"""
            self.height = height

        @property
        def x(self):
            """x getter """
            return self.x

        @x.setter
        def x(self, x):
            """ x setter"""
            self.x = x

        @property
        def y(self):
            """y getter """
            return self.y

        @y.setter
        def y(self, y):
            """ y setter"""
            self.y = y

        @property
        def id(self):
            return self.id

        @id.setter
        def id(self, id):
            """ height setter"""
            self.id = id
