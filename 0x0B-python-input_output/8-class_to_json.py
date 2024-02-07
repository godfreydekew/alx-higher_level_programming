#!/usr/bin/python3
"""Define class_to_json function"""


def class_to_json(obj):
    """Returns dictionary description of an object"""
    return obj.__dict__
