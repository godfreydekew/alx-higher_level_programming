#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Inherits  from list class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted([self.__getitem__(i) for i in range(self.__len__())]))
