#!/usr/bin/python3
"""Defines Student class"""


class Student:
    """A class showing Student"""

    def __init__(self, first_name, last_name, age):
        """

           """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): A list of attribute names to include
                 in the dictionary. If not provided, include all attributes.

        Returns:
            dict: A dictionary containing attribute names and values.
        """
        if (type(attrs)) == list and all(isinstance(s, str) for s in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attribute of a Student."""
        for key, value in json.items():
            setattr(self, key, value)
