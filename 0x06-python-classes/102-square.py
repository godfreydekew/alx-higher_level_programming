#!/usr/bin/python3
"""Defining the class called Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        self.__size = size
        """Method to initialize a new instance of Square.

        Args:
            size (int): The size of the square.
        """

    def area(self):
        """Method that calculates are"""
        return int(self.__size) * int(self.__size)

    @property
    def size(self):
        """Retrieves the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Checks if the value of size is valid"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def __eq__(self, other):
        """Checks if area() is == other.area()"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if the area of the current square is
        not equal to the area of another square."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Check if the area of the current square is
        greater than the area of another square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if the area of the current square is greater
         than or equal to the area of another square."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Check if the area of the current square is
        less than the area of another square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if the area of the current square is
         less than or equal to the area of another square."""
        return self.area() <= other.area()
