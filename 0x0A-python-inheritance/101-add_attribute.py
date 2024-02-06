#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, my_attr, value):
    """Add a new attribute to an object.

    Args:
        obj (any): The object to add an attribute to.
        my_attr (str): The name of the attribute to add.
        value (any): The value of the attribute.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, my_attr, value)
