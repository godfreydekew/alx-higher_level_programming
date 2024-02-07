#!/usr/bin/python3
"""Defines append_after function."""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends new_string after the first occurrence of search_string in the file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The string to append after the search_string.

    Returns:
        None
    """
    with open(filename, mode='r', encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, mode='w', encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
