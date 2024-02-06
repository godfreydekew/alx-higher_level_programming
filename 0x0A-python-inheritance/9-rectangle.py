#!/usr/bin/python3
"""Defines the Rectangle class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    Inherits from:
    - BaseGeometry: Provides basic geometry-related methods.

    Attributes:
    - __width (int): The width of the rectangle.
    - __height (int): The height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with the given
         width and height.

        Args:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.

        Raises:
        - TypeError: If width or height is not an integer.
        - ValueError: If width or height is less than or equal to 0.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
        - int: The calculated area.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a human-readable string representation of the
         Rectangle instance.

        Returns:
        - str: A formatted string representing the instance.
        """
        s = self.__height
        return "[{}] {}/{}".format(type(self).__name__, self.__width, s)
