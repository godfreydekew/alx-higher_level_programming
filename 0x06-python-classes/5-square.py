#!/usr/bin/python3
"""Defining the class called Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        self.size = size
        """Method to initialize a new instance of Square.

        Args:
            size (int): The size of the square.
        """

    def area(self):
        """Method that calculates area"""
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

    def my_print(self):
        """Prints the square with '#' to the stdout."""
        if self.__size != 0:
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
            return
