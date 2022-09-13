#!/usr/bin/python3
"""defines a MagicClass"""
import math


class MagicClass:
    """This represents a class for circle attributes"""
    def __init__(self, radius=0):
        """Initializes the MagicClass method"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """Calculaes the area of a circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculates the circumference of a circle"""
        return (2 * math.pi * self.__radius)
