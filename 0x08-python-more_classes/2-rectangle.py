#!/usr/bin/python3
"""Defining the class called rectangle."""


class Rectangle:
    """The rectangle class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """Checks if the value of width is valid"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Checks if the value of height is valid"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """Method that calculates area"""
        return int(self.__height) * int(self.__width)

    def perimeter(self):
        """Method that calculates perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (int(self.__height) + int(self.__width))
