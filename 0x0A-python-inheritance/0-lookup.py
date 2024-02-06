#!/usr/bin/python3
"""function that returns the list of available
 attributes and methods of an object
 """


def lookup(obj):
    """
    Get a list of names in the namespace of an object.

    Parameters:
    - obj: Any Python object.

    Returns:
    - A list containing names in the namespace of the given object.
    - This includes attributes, methods, and other objects
        associated with the object.

    """
    return dir(obj)
