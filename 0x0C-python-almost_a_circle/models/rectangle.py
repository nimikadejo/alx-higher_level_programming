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

