#!/usr/bin/python3
"""Defines read_file function"""


def read_file(filename=""):
    """Reads and prints the content of a text file.

        Args:
            filename (str): The name of the file to be read.

        Returns:
            None
        """
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end="")
