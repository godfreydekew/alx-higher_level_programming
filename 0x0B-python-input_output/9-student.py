#!/usr/bin/python3
"""Defines Student class"""


class Student:
    """A class showing Student"""
    def __init__(self, first_name, last_name, age):
        """
           A class representing a Student.

           Parameters:
           - first_name (str): The first name of the student.
           - last_name (str): The last name of the student.
           - age (int): The age of the student.
           """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
