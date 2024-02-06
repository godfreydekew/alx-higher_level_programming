#!/usr/bin/python3
"""Defines   BaseGeometry """


class BaseGeometry:
    """
            Validates if a given value is an integer and greater than 0.

            Args:
            - name (str): The name of the value being validated.
            - value: The value to be validated.

            Raises:
            - TypeError: If the value is not an integer.
            - ValueError: If the value is less than or equal to 0.
            """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
