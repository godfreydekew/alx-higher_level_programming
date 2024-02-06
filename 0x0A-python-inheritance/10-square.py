#!/usr/bin/python3
"""Defines Square class that inherites from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square.

    Inherits from:
    - Rectangle: Represents a rectangle and inherits
    its attributes and methods.

    Attributes:
    - __size (int): The size of the square.
    """
    def __init__(self, size):
        """
        Initializes a Square instance with the given size.

        Args:
        - size (int): The size of the square.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than or equal to 0.
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
