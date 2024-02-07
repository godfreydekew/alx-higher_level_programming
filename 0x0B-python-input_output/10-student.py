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
        if attrs and all(isinstance(s, str) for s in attrs):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__
