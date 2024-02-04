#!/usr/bin/python3
"""Defining the class called rectangle."""


class Rectangle:
    """The rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """
               Return a string representation of the
                rectangle using '#' characters.

               Returns:
                   str: String representation of the rectangle.
               """
        hash_string = ""
        if self.height == 0 or self.width == 0:
            return ""
        else:
            for i in range(self.height):
                for x in range(self.width):
                    hash_string += str(self.print_symbol)
                hash_string += "\n"
            my_string = f"{hash_string}"
            return my_string[:-1]

    def __repr__(self):
        """
            Return a string representation that
            can be used to recreate the rectangle.

            Returns:
                str: String representation of the
                 rectangle for reproduction.
            """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        """
            Destructor: Prints farewell message
            on rectangle deletion.
        """
        print("Bye rectangle...")
