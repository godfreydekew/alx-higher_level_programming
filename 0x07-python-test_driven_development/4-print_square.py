#!/usr/bin/python3
"""A function that prints a string."""


def print_square(size):
    """
       Prints a square made of '#' characters with the specified size.

       Parameters:
       - size (int): The size of the square. Must be a non-negative integer.

       Raises:
       - TypeError: If `size` is not an integer.
       - TypeError: If `size` is a negative float.
       - ValueError: If `size` is a negative integer.

       """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for i in range(size)]
        print()
