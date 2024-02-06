#!/usr/bin/python3
"""Defines   Rectangle class """
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


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
