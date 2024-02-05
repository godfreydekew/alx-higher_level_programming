#!/usr/bin/python3
"""A function that prints a string."""


def say_my_name(first_name, last_name=""):
    """
       Prints a formatted string representing a person's name.

       Parameters:
       - first_name (str): The first name of the person.
       - last_name (str, optional): The last name of the
        person. Defaults to an empty string.

       Raises:
       - TypeError: If either `first_name` or `last_name` is not a string.
       """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
