#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """
    A custom integer class with reversed equality operators.

    Inherits from:
    - int: Python's built-in integer class.

    Methods:
    - __eq__: Overrides the equality operator to return the negation
    of the superclass's equality.
    - __ne__: Overrides the inequality operator to return the
    negation of the superclass's inequality.
    """
    def __eq__(self, other):
        """Overrides the equality operator."""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Overrides the inequality operator."""
        return not super().__ne__(other)
