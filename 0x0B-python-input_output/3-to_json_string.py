#!/usr/bin/python3
"""Defines to_json_string"""
import json


def to_json_string(my_obj):
    """
     returns the JSON representation of an object (string):
    :param my_obj:
        object or string
    :return:
        json string
    """
    return json.dumps(my_obj)
